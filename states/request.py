from aiogram.dispatcher.filters.state import State, StatesGroup

class Request(StatesGroup):
    user_name = State()
    req_type = State()
    description = State()
    created_at = State()