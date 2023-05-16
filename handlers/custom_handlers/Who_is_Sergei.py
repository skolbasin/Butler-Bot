from run import Mr_Butler, bot
from aiogram.types import message
from keyboards.inline_keyboards import inline_kb

@Mr_Butler.message_handler(commands=['who'])
async def hi(message: message):
    await bot.send_photo(message.from_user.id,
                         photo=open('foto/prog.jpg', 'rb'),
                         caption='Господин учится на <b>программиста</b>\n'
                                 'Учит он язык Python 🐍 и уже в ближайшее время станет backend-разработчиком🤓\n\n'
                                 'Я подготовил для Вас 3 статьи, после прочтения которых Вам все станет понятно😉\n\n'
                                 'Также Вы можете посмотреть видео на канале Сергея, он там все-все рассказывает\n'
                                 f'{" " * 32 } ⬇⬇⬇',
                         reply_markup=inline_kb, parse_mode='html')
