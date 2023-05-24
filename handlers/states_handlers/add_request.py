import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.reply_keyboards import reply_kb2
from run import Mr_Butler, bot
from states.request import Request
from datetime import datetime
from utils.all_pattern import telephone_pattern, data_pattern
from utils.time_of_day import check_daytime
from database.sqlite_db import db_table_val


@Mr_Butler.message_handler(lambda message: 'req' in message.text)
async def user_register(message: types.Message):
    await bot.send_photo(message.from_user.id,
                        photo=open('foto/req.png', 'rb'),
                        caption="Вы можете оставить заявку на любую тему, а я ее передам Сергею в самое ближайшее время😉\n"
                         "Для начала, введите, пожалуйста, <b>Ваше имя</b> ",
                        parse_mode='html')
    await Request.user_name.set()


# Первый вопрос
@Mr_Butler.message_handler(state=Request.user_name)
async def get_user_name(message: types.Message, state: FSMContext):
    await state.update_data(user_name=message.text)
    await message.answer(f"Отлично, {message.text}!\n"
                               f"Теперь нужно выбрать <b>тип обращения:</b>\n\n"
                               f"1. Приглашение на встречу\n"
                               f"2. Попросить набрать\n"
                               f"3. Зашифровать послание на языке 'Присивесет'\n"
                               f"4. Другое\n\n"
                               f"Выберите цифру от 1 до 4",
                               parse_mode='html', reply_markup=reply_kb2)
    await Request.next()

# Второй вопрос
@Mr_Butler.message_handler(state=Request.req_type)
async def get_req_type(message: types.Message, state: FSMContext):
    if message.text == '1':
        await state.update_data(req_type=message.text)
        await message.answer("Напишите, пожалуйста, когда бы хотели встретиться.\n"
                             "Формат: <b>01.01.2023 14:30</b>", parse_mode='html')
        await Request.next()
    elif message.text == '2':
        await state.update_data(req_type=message.text)
        await message.answer("Напишите, пожалуйста, <b>Ваш номер телефона</b> в формате 8(YYY)XXX XX XX\n"
                             "Пример: 89991234567", parse_mode='html')
        await Request.next()
    elif message.text == '3':
        await state.update_data(req_type=message.text)
        await message.answer("Введите зашифрованный текст")
        await Request.next()
    elif message.text == '4':
        await state.update_data(req_type=message.text)
        await message.answer("Укажите, что именно Вас интересует, я Все передам в точности от слова к слову!")
        await Request.next()
    else:
        await message.answer('Дорогой друг, напиши, пожалуйста, цифру от 1 до 4, '
                             'в зависимости от того, какой тип заявки ты хочешь оставить. Спасибо!')


# Третий вопрос
@Mr_Butler.message_handler(state=Request.description)
async def get_description(message: types.Message, state: FSMContext):
        answer = await state.get_data()
        await state.update_data(description=message.text, created_at=datetime.now())
        data = await state.get_data()
        if answer['req_type'] == '1'and re.match(data_pattern, message.text) is not None:
            await message.answer(f"Отлично! Передам Сергею, что вы хотите встретиться {message.text}.\n{check_daytime()}", parse_mode='html')
            await state.finish()
        elif answer['req_type'] == '1'and re.match(data_pattern, message.text) is None:
            await message.answer(f"{data['user_name']}, пожалуйста, введите дату в корректном формае")
        elif answer['req_type'] == '2' and re.match(telephone_pattern, message.text) is not None:
            await message.answer(f"Отлично! Передам Ваши контакты\nСергей наберет Вас как только освободиться.\n{check_daytime()}")
            await state.finish()
        elif answer['req_type'] == '2' and re.match(telephone_pattern, message.text) is None:
            await message.answer(f"{answer['user_name']}, введите, пожалуйста, номер телефона в том формате, который я указал выше. Спасибо!")
        elif answer['req_type'] == '3':
            await message.answer(f"Передам Ваш шифр Сергею.\n{check_daytime()}")
            await state.finish()
        elif answer['req_type'] == '4':
            await message.answer(f"Хорошо. Передам Ваш запрос.\n{check_daytime()}'")
            await state.finish()

        db_table_val(user_name=data['user_name'], req_type=data['req_type'], description=data['description'], created_at=data['created_at'])

