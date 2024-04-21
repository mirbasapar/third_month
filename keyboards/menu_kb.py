from aiogram import types


def menu_kb():
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Закуски'),
            types.KeyboardButton(text='Салаты')],
            [types.KeyboardButton(text='Супы'),
            types.KeyboardButton(text='Открытый огонь и Хоспер')],
            [types.KeyboardButton(text='Сезоны Кыргызстана'),
            types.KeyboardButton(text='Мясо, Рыба, Птица')],
            [types.KeyboardButton(text='Гарниры'),
            types.KeyboardButton(text='На Компанию')],
            [types.KeyboardButton(text='Десерты'),
            types.KeyboardButton(text='Хлеб и Выпечка')]
        ]
    )
    return kb



