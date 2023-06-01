from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_1 = [
            KeyboardButton('Отправить контакты Сергею для связи', request_contact=True),
            KeyboardButton('Отправить геолокацию', request_location=True),
             ]
reply_kb.row(*buttons_1)

cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_2 = [
    KeyboardButton('Выйти'),
    KeyboardButton('Подсказка'),
    ]
cancel_kb.row(*buttons_2)

reply_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_3 = [
    KeyboardButton('1'),
    KeyboardButton('2'),
    KeyboardButton('3'),
    KeyboardButton('4'),
    ]
reply_kb2.row(*buttons_3)

reply_kb3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_4 = [
    KeyboardButton('Да'),
    KeyboardButton('Нет')
    ]
reply_kb3.row(*buttons_4)