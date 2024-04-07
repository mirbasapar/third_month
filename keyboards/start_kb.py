from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Наш адрес', callback_data='adress')],
        [InlineKeyboardButton(text='Контакты', callback_data='contact')],
        [InlineKeyboardButton(text='О нас', url='https://barashek.kg/o-nas/')],
        [InlineKeyboardButton(text='Наш сайт', url='https://barashek.kg/')],
        [InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/barashek.restaurant/')],
        [InlineKeyboardButton(text='Наше меню', callback_data='menu')]
    ])
    return kb