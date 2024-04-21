from aiogram import types


def start_kb():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Наш адрес', callback_data='adress'),
            types.InlineKeyboardButton(text='Контакты', callback_data='contact')],
            [types.InlineKeyboardButton(text='О нас', url='https://barashek.kg/o-nas/'),
            types.InlineKeyboardButton(text='Наш сайт', url='https://barashek.kg/')],
            [types.InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/barashek.restaurant/'),
            types.InlineKeyboardButton(text='Наше меню', callback_data='menu')],
            [types.InlineKeyboardButton(text='Оставить отзыв', callback_data='review')]
        ]
    )
    return kb


