from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

inline_kb = InlineKeyboardMarkup(row_width=1)
buttons = [InlineKeyboardButton(text='Статья №1 (Программирование)', url='https://blog.skillfactory.ru/programmirovanie-chto-takoe/'),
            InlineKeyboardButton(text='Статья №2 (Python)', url='https://aws.amazon.com/ru/what-is/python/'),
            InlineKeyboardButton(text='Статья №3 (Backend-разработка)', url='https://habr.com/ru/companies/ruvds/articles/488340/'),
            InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/channel/UCaW0RNRwMILFdRM3-EpUYjg')
           ]
inline_kb.add(*buttons)

inline_kb2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Что я могу', callback_data='cb1'))

inline_kb3 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='👍', callback_data='form1'),
                                                   InlineKeyboardButton(text='👎', callback_data='form2'))




