from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton('Отправить контакты Сергею для связи', request_contact=True)
b2 = KeyboardButton('Отправить геолокацию', request_location=True)
b3 = KeyboardButton('/Где_Сергей')
b4 = KeyboardButton('/Кто_родился_у_Сергея')

reply_kb.row(b1, b2)
reply_kb.row(b3, b4)