from aiogram.dispatcher.filters.state import State, StatesGroup

class Quiz(StatesGroup):
    name = State()
    first_answer = State()
    second_answer = State()
    third_answer = State()
    fourth_answer = State()
