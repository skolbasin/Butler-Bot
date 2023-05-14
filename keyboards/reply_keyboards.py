from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton('Отправить контакты Сергею для связи', request_contact=True)
b2 = KeyboardButton('Отправить геолокацию', request_location=True)
b3 = KeyboardButton('/Где_Сергей')
b4 = KeyboardButton('/Кто_родился_у_Сергея')
b5 = KeyboardButton('/На_кого_учится_Сергей')
b6 = KeyboardButton('/Викторина')

reply_kb.row(b1, b2)
reply_kb.row(b3, b4)
reply_kb.row(b5, b6)