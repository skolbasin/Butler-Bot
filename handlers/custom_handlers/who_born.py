from run import Mr_Butler, bot
from aiogram.types import message
from keyboards.reply_keyboards import reply_kb
from datetime import date
from utils.date_transformation import transformation_date

birthday = date(2023, 4, 25)
current_day = date.today()
difference = current_day - birthday

@Mr_Butler.message_handler(commands=['born'])
async def hi(message: message):
    await bot.send_photo(message.from_user.id,
                         photo=open('foto/baby.jpg', 'rb'),
                         caption=f'Родилась девочка\n'
                                 f'Звать <b>Алина</b> 👶\n'
                                 f'Сегодня {transformation_date(str(current_day))}, а значит Алине сейчас {difference.days} дней🥳',
                         reply_markup=reply_kb, parse_mode='html')