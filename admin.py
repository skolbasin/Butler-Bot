from aiogram import types

from database.sqlite_db import check_db, read_db
from keyboards.inline_keyboards import inline_kb4
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

@Mr_Butler.message_handler(commands='Редактировать')
async def all_requests(message: types.message):
    if message.from_user.id == ID:
        request_list = await read_db()
        count = 0
        for i_req in request_list:
            count += 1
            await bot.send_message(message.from_user.id, text=f'<b>Заявка {count}</b>\n{i_req}', reply_markup=inline_kb4, parse_mode='html')


