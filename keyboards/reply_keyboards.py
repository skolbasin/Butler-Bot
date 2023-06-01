from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('Отправить контакты Сергею для связи', request_contact=True)
b2 = KeyboardButton('Отправить геолокацию', request_location=True)
reply_kb.row(b1, b2)

cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('Выйти')
b2 = KeyboardButton('Подсказка')
cancel_kb.row(b1, b2)

reply_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons = [
            KeyboardButton('1'), KeyboardButton('2'),
            KeyboardButton('3'), KeyboardButton('4')
        ]
reply_kb2.row(*buttons)


reply_kb3 =  ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('Да')
b2 = KeyboardButton('Нет')
reply_kb3.row(b1, b2)