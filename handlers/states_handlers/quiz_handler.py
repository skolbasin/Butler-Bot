from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.reply_keyboards import cancel_kb
from run import Mr_Butler, bot
from states.quiz import Quiz


# Старт игры
@Mr_Butler.message_handler(commands=['quiz'])
async def user_register(message: types.Message):
    await message.answer("Рад приветствовать Вас на Викторине <b>'За знания - ДА!'</b>\n"
                         "Пожалуйста, введите Ваше имя для начала игры", parse_mode='html')
    await Quiz.name.set()

# Выход из игры
@Mr_Butler.message_handler(state='*', commands='Выйти')
@Mr_Butler.message_handler(Text(equals='Выйти', ignore_case=True), state='*')
async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    print(type(current_state))
    if current_state is None:
        return None
    await state.finish()
    await message.reply('Буду ждать, что бы еще раз сыграть!')

# Получение подсказки
@Mr_Butler.message_handler(state='*', commands='Подсказка')
@Mr_Butler.message_handler(Text(equals='Подсказка', ignore_case=True), state='*')
async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return None
    elif current_state == 'Quiz:first_answer':
        await message.reply('Он еще немножечко любил выпить и в его честь назван музей-центр в Москве')
    elif current_state == 'Quiz:second_answer':
        await message.reply('3 буквы, почти как дуб')
    elif current_state == 'Quiz:third_answer':
        await message.reply('Найди ее здесь https://skysmart.ru/articles/mathematic/formuly-sokrashennogo-umnozheniya')
    elif current_state == 'Quiz:fourth_answer':
        await message.reply('Кто любит мёд, кроме медведей? И в уменьшительно-ласкательном, пожалуйста')

# Первый вопрос
@Mr_Butler.message_handler(state=Quiz.name)
async def get_first_answer(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await bot.send_photo(message.from_user.id,
                         photo=open('foto/saw.jpg', 'rb'),
                         caption=f"Отлично, {message.text}! Теперь давайте играть.\n"
                         "<u>Вопрос 1.</u> Как звали первого президента РФ? (Фамилия)",
                         parse_mode='html', reply_markup=cancel_kb)
    await Quiz.next()

# Второй вопрос
@Mr_Butler.message_handler(state=Quiz.first_answer)
async def get_second_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == 'ельцин':
        await state.update_data(first_answer=message.text)
        await message.answer("Верно!🥳\n"
                             "Давайте двигаться дальше.\n"
                             "<u>Вопрос 2.</u>Как геймеры называют игрока, который не умеет играть?",
                             parse_mode='html', reply_markup=cancel_kb)
        await Quiz.next()
    elif message.text.lower() == 'ельцын':
        await state.update_data(first_answer=message.text)
        await message.answer("Ну вообще он 'Ельц<b>И</b>н', но засчитаем как верно🤫\n"
                             "Давайте двигаться дальше.\n"
                             "<u>Вопрос 2.</u>Как геймеры называют игрока, который не умеет играть?\n(3 БУКВА)",
                             parse_mode='html', reply_markup=cancel_kb)
        await Quiz.next()
    else:
        await message.answer('К сожалению, это неверный ответ, подумайте еще. Как надумаете, приходите играть заново.')
        await state.finish()

# Третий вопрос
@Mr_Butler.message_handler(state=Quiz.second_answer)
async def get_third_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == 'нуб':
        await state.update_data(second_answer=message.text)
        await bot.send_photo(message.from_user.id,
                             photo=open('foto/formula.jpg', 'rb'),
                             caption="Отлично! Всем нам приходилось играть с ними. Едем дальше .\n"
                                    "<u>Вопрос 3.</u>Как называется формула. решение которой представлено на фото?\n"
                                    "P.S. А Вы думали мы тут шутки шутить будем?",
                             parse_mode='html', reply_markup=cancel_kb)

        await Quiz.next()
    else:
        await message.answer(f'К сожалению, это неверный ответ, подумайте еще. Как надумаете, приходите играть заново.')
        await state.finish()

# Четвертый вопрос
@Mr_Butler.message_handler(state=Quiz.third_answer)
async def get_username(message: types.Message, state: FSMContext):
    if message.text.lower() == 'формула квадрата разности':
        await state.update_data(third_answer=message.text)
        await bot.send_photo(message.from_user.id,
                             photo=open('foto/respect.jpg', 'rb'),
                             caption="Воу.Моё почтение сударь!\n"
                                     "Остался последний вопрос, над ним билось группа ученых и Гарворда, но так и не нашли верноый ответ"
                                     "<u>Вопрос 4.</u> 'Жалко у..'",
                             parse_mode='html', reply_markup=cancel_kb)
        await Quiz.next()
    elif message.text.lower() == 'квадрата разности':
        await state.update_data(third_answer=message.text)
        await bot.send_photo(message.from_user.id,
                             photo=open('foto/respect.jpg', 'rb'),
                             caption="Воу.Моё почтение сударь!\n"
                                    "Остался последний вопрос, над ним билось группа ученых и Гарворда, но так и не нашли верноый ответ"
                                    "<u>Вопрос 4.</u> 'Жалко у..'",
                             parse_mode='html', reply_markup=cancel_kb)
        await Quiz.next()
    else:
        await message.answer('Не совсем так,  подумайте еще. Как надумаете, приходите играть заново.')
        await state.finish()

# Конец игры
@Mr_Butler.message_handler(state=Quiz.fourth_answer)
async def get_fourth_answer(message: types.Message, state: FSMContext):
    response_list = ['пчелка', 'пчелки', 'пчёлка', 'пчёлка']
    if message.text.lower() in response_list:
        await state.update_data(fourth_answer=message.text)
        data = await state.get_data()
        await bot.send_photo(message.from_user.id,
                             photo=open('foto/bee.jpg', 'rb'),
                             caption="Поздравляю, Вы победили в Викторине!\n"
                                    f"Вы знаете, что {data['first_answer']} был первым президентом РФ\n"
                                    f"Хотя бы раз играли в команде, где есть господин {data['second_answer']}\n"
                                    f"Шарите за математику\n"
                                    f"И знаете что не друга жалко, когда он потратил все деньги на ставки на спорт"
                                    f",а жалко может быть только у {data['fourth_answer']}\n"
                                    f"Вы лучший!")

    else:
        await message.answer('К сожалению, это неверный ответ, подумайте еще. Как надумаете, приходите играть заново.')
    await state.finish()

