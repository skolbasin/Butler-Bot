from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb = InlineKeyboardMarkup(row_width=3)

b1 = InlineKeyboardButton(text='Статья №1 (Программирование)', url='https://blog.skillfactory.ru/programmirovanie-chto-takoe/')
b2 = InlineKeyboardButton(text='Статья №2 (Python)', url='https://aws.amazon.com/ru/what-is/python/')
b3 = InlineKeyboardButton(text='Статья №3 (Backend-разработка)', url='https://habr.com/ru/companies/ruvds/articles/488340/')
b4 = InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/channel/UCaW0RNRwMILFdRM3-EpUYjg')

inline_kb.add(b1)
inline_kb.add(b2)
inline_kb.add(b3)
inline_kb.add(b4)