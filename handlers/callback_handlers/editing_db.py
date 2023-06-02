from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from database import sqlite_db
from run import Mr_Butler, bot


@Mr_Butler.callback_query_handler(Text(startswith='change'))
async def delete(callback: CallbackQuery):
    if callback.data == 'change2':
        req_id = callback.message.text[10]
        await sqlite_db.delete_db(req_id)
        await bot.send_message(callback.from_user.id, text=f'Заявка c ID {req_id} успешно удалена')

