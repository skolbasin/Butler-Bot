from run import Mr_Butler, bot
from aiogram.types import message
from keyboards.inline_keyboards import inline_kb2
from handlers.callback_handlers import bot_info

@Mr_Butler.message_handler(commands=['start'])
async def hi(message: message):
    await bot.send_photo(message.from_user.id,
                         photo=open('foto/robot.jpg', 'rb'),
                         caption=f'Привет, дорогой друг!🖖\n'
                                 'Я бот-дворецкий 🤵‍♂️ его величества Сергея Колбасина-младшего.🫅\n'
                                 'Ходят слухи 👀 что у моего господина родилась дочка 👶, поэтому он теперь редко выходит на связь\n'
                                 'Так что теперь я за него 🤷‍♂\n'
                                 'Но Вы не переживайте!!! Это не надолго, всего лет на 5-10😉\n'
                                 'А пока Вы можете пообщаться со мной, потыкав меню!😇', reply_markup=inline_kb2)