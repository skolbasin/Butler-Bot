from aiogram.types import CallbackQuery
from run import Mr_Butler, bot

@Mr_Butler.callback_query_handler(text='cb1')
async def get_info(callback: CallbackQuery):
    await bot.answer_callback_query(callback.id, '1. Могу рассказать тебе о Сергее, где он сейчас и о его дочке\n'
                                                 '2. Могу сыграть с тобой в викторину\n'
                                                 '3. Могу оставить заявку Сергею', show_alert=True)