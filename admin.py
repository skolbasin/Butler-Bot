from aiogram import types
from loader import Mr_Butler, bot
ID = None

@Mr_Butler.message_handler(commands=['administrator'], is_chat_admin=True)
async def chech_admin(message: types.message):
    global ID
    ID = message.from_user.id
    await message.answer(f'Ваш ID {ID}\nВы являетесь администратором этой группы')




