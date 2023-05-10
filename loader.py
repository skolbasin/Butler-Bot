from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage # просто, хранящее информацию в ОП
from dotenv import load_dotenv, find_dotenv
import os

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
Mr_Butler = Dispatcher(bot, storage=storage)


async def set_default_commands(dp):
    print('Бот запустился, всё отлично')
    await dp.bot.set_my_commands([
        BotCommand("start", "Запустить бота"),
    ])

