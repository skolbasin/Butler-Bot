from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from run import Mr_Butler, bot

@Mr_Butler.callback_query_handler(Text(startswith='form'))
async def like(callback: CallbackQuery):
    if callback.data == 'form1':
        await bot.answer_callback_query(callback.id, 'Спасибо. Алине будет очень приятно❤', show_alert=False)
    else:
        await bot.answer_callback_query(callback.id, 'Поздравляю, Вы в черном списке! ', show_alert=False)