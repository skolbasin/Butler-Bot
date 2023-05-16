from aiogram import types
from aiogram.dispatcher import FSMContext
from run import Mr_Butler, bot
from states.quiz import Quiz


@Mr_Butler.message_handler(commands=['quiz'])
async def user_register(message: types.Message):
    await message.answer("Рад приветствовать Вас на Викторине <b>'За знания - ДА!'</b>\n"
                         "Пожалуйста, введите Ваше имя для начала игры", parse_mode='html')
    await Quiz.name.set()

@Mr_Butler.message_handler(state=Quiz.name)
async def get_first_answer(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await bot.send_photo(message.from_user.id, photo=open('foto/saw.jpg', 'rb'), caption=f"Отлично, {message.text}! Теперь давайте играть.\n"
                         "<u>Вопрос 1.</u> Как звали первого президента РФ? (Фамилия)", parse_mode='html')
    await Quiz.next()

@Mr_Butler.message_handler(state=Quiz.first_answer)
async def get_second_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == 'ельцин':
        await state.update_data(first_answer=message.text)
        await message.answer("Верно!🥳\n"
                             " Давайте двигаться дальше.\n"
                             "<u>Вопрос 2.</u>Как геймеры называют игрока, который не умеет играть?", parse_mode='html')
        await Quiz.next()
    elif message.text.lower() == 'ельцын':
        await state.update_data(first_answer=message.text)
        await message.answer("Ну вообще он 'Ельц<b>И</b>н', но засчитаем как верно🤫\n"
                             "Давайте двигаться дальше.\n"
                             "<u>Вопрос 2.</u>Как геймеры называют игрока, который не умеет играть?\n(3 БУКВА)", parse_mode='html')
        await Quiz.next()
    else:
        await message.answer('К сожалению, это неверный ответ, подумайте еще. Как надумаете, приходите играть заново.')
        await state.finish()

@Mr_Butler.message_handler(state=Quiz.second_answer)
async def get_third_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == 'нуб':
        await state.update_data(second_answer=message.text)
        await bot.send_photo(message.from_user.id, photo=open('foto/formula.jpg', 'rb'), caption="Отлично! Всем нам приходилось играть с ними. Едем дальше .\n"
                         "<u>Вопрос 3.</u>Как называется формула. решение которой представлено на фото?\n"
                             "P.S. А Вы думали мы тут шутки шутить будем?", parse_mode='html')

        await Quiz.next()
    else:
        await message.answer(f'К сожалению, это неверный ответ, подумайте еще. Как надумаете, приходите играть заново.')
        await state.finish()

@Mr_Butler.message_handler(state=Quiz.third_answer)
async def get_username(message: types.Message, state: FSMContext):
    if message.text.lower() == 'формула квадрата разности':
        await state.update_data(third_answer=message.text)
        await bot.send_photo(message.from_user.id, photo=open('foto/respect.jpg', 'rb'),
                             caption="Воу.Моё почтение сударь!\n"
                                     "Остался последний вопрос, над ним билось группа ученых и Гарворда, но так и не нашли верноый ответ"
                                     "<u>Вопрос 4.</u> 'Жалко у..'", parse_mode='html')
        await Quiz.next()
    elif message.text.lower() == 'квадрата разности':
        await state.update_data(third_answer=message.text)
        await bot.send_photo(message.from_user.id, photo=open('foto/respect.jpg', 'rb'), caption="Воу.Моё почтение сударь!\n"
                                                                                                 "Остался последний вопрос, над ним билось группа ученых и Гарворда, но так и не нашли верноый ответ"
                                                                                                "<u>Вопрос 4.</u> 'Жалко у..'", parse_mode='html')
        await Quiz.next()
    else:
        await message.answer('Не совсем так,  подумайте еще. Как надумаете, приходите играть заново.')
        await state.finish()

@Mr_Butler.message_handler(state=Quiz.fourth_answer)
async def get_fourth_answer(message: types.Message, state: FSMContext):
    if message.text.lower() == 'пчелки' or message.text.lower() == 'пчёлки':
        await state.update_data(fourth_answer=message.text)
        data = await state.get_data()
        await bot.send_photo(message.from_user.id, photo=open('foto/bee.jpg', 'rb'), caption="Поздравляю, Вы победили в Викторине!\n"
                                                                                             f"Вы знаете, что {data['first_answer']} был первым президентом РФ\n"
                                                                                             f"Хотя бы раз играли в команде, где есть господин {data['second_answer']}\n"
                                                                                             f"Шарите за математику\n"
                                                                                             f"И знаете что не друга жалко, когда он потратил все деньги на ставки на спорт"
                                                                                             f",а жалко может быть только у {data['fourth_answer']}\n"
                                                                                             f"Вы лучший!")
    else:
        await message.answer('К сожалению, это неверный ответ, подумайте еще. Как надумаете, приходите играть заново.')
        await state.finish()