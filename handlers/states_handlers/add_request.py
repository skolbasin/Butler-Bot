from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.reply_keyboards import reply_kb2
from run import Mr_Butler, bot
from states.request import Request
from datetime import datetime


@Mr_Butler.message_handler(lambda message: 'req' in message.text)
async def user_register(message: types.Message):
    await bot.send_photo(message.from_user.id,
                        photo=open('foto/req.png', 'rb'),
                        caption="Вы можете оставить заявку на любую тему, а я ее передам Сергею в самое ближайшее время😉\n"
                         "Для начала, введите, пожалуйста, Ваше <b>имя</b> ",
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
        await message.answer("Напишите, пожалуйста, когда бы хотели встретиться")
        await Request.next()
    elif message.text == '2':
        await state.update_data(req_type=message.text)
        await message.answer("Напишите, пожалуйста, Ваш номер телефона в формате <b>8 (YYY) XXX XX XX</b>",
                             parse_mode='html')
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
        await state.update_data(description=message.text, created_at=datetime.now())
        data = await state.get_data()
        await message.answer("Отлично! Ваша заявка сформирована")
        await state.finish()


