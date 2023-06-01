from aiogram import types

from database.sqlite_db import check_db
from loader import Mr_Butler, bot

ID = None

@Mr_Butler.message_handler(commands=['administrator'], is_chat_admin=True)
async def chech_admin(message: types.message):
    global ID
    ID = message.from_user.id
    await message.answer(f'Ваш ID {ID}\nВы являетесь администратором этой группы')

@Mr_Butler.message_handler(commands='Заявки')
async def all_requests(message: types.message):
    if message.from_user.id == ID:
        await check_db(message)
