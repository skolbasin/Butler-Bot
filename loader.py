# создаем самого бота и пространство для хранения информации
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
import os

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


bot = Bot(token=os.getenv('TOKEN'))
Mr_Butler = Dispatcher(bot)
storage = MemoryStorage()

async def set_default_commands(dp):
    print('Бот запустился, всё отлично')
    await dp.bot.set_my_commands([
        BotCommand("start", "Запустить бота"),
        BotCommand("try", "Попробуй"),
    ])

проверака