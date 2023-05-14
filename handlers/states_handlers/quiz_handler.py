from aiogram import types
from aiogram.dispatcher import FSMContext
from run import Mr_Butler, bot
from states.quiz import Quiz


@Mr_Butler.message_handler(commands=['Викторина'])
async def user_register(message: types.Message):
    await message.answer("Рад приветствовать Вас на Викторине <b>'За знания - ДА!'</b>\n"
                         "Пожалуйста, введите Ваше имя для начала игры", parse_mode='html')
    await Quiz.name.set()

@Mr_Butler.message_handler(state=Quiz.name)
async def get_first_answer(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично! Теперь давайте играть.\n"
                         "Вопрос 1.")
    await Quiz.next()

@Mr_Butler.message_handler(state=Quiz.first_answer)
async def get_second_answer(message: types.Message, state: FSMContext):
    await state.update_data(first_answer=message.text)
    await message.answer("Отлично! Теперь давайте играть.\n"
                         "Вопрос 2.")
    await Quiz.next()

@Mr_Butler.message_handler(state=Quiz.second_answer)
async def get_third_answer(message: types.Message, state: FSMContext):
    await state.update_data(second_answer=message.text)
    await message.answer("Отлично! Теперь давайте играть.\n"
                         "Вопрос 3.")
    await Quiz.next()

@Mr_Butler.message_handler(state=Quiz.third_answer)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(third_answer=message.text)
    await message.answer("Отлично! Теперь давайте играть.\n"
                         "Вопрос 4.")
    await Quiz.next()

@Mr_Butler.message_handler(state=Quiz.fourth_answer)
async def get_fourth_answer(message: types.Message, state: FSMContext):
    await state.update_data(fourth_answer=message.text)
    data = await state.get_data()
    await message.answer("Конец игры.")

    await state.finish()