from run import Mr_Butler, bot
from aiogram.types import message
from keyboards.reply_keyboards import reply_kb

@Mr_Butler.message_handler(lambda message: 'where' in message.text)
async def hi(message: message):
    await bot.send_photo(message.from_user.id,
                         photo=open('foto/young_father.jpg', 'rb'),
                         caption='Господин попросил отправить данное фото, вместо 1000 слов и одной постоянно меняющейся геолокации',
                         reply_markup=reply_kb)