from aiogram.utils import executor # чтоб бот вышел в онлайн-пространство
from loader import set_default_commands
from loader import Mr_Butler
from loader import bot # чтоб подгружался сам бот
import handlers # чтоб подгружались хендлеры


if __name__ == '__main__':
    executor.start_polling(Mr_Butler, skip_updates=True, on_startup=set_default_commands)
# чтоб работал в long_polling режиме
# skip_updates - чтоб бот не отвечал на сообщения, когда выйдетна связь(на сообщения, которые были написаны когда бот оффлайн)
# on_startup - чтоб запускал меню с возможными командами