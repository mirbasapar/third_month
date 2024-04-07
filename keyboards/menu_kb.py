from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Первые блюдо'),
         KeyboardButton(text='Вторые блюда')],
        [KeyboardButton(text='Десерт'),
         KeyboardButton(text='Напитки')],
    ],
    one_time_keyboard=True,
    resize_keyboard=True)
    return kb