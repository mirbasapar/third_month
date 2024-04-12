from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from handlers.callback import snacks

def menu_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Закуски'),
            KeyboardButton(text='Салаты')],
            [KeyboardButton(text='Супы'),
            KeyboardButton(text='Открытый огонь и Хоспер')],
            [KeyboardButton(text='Сезоны Кыргызстана'),
            KeyboardButton(text='Мясо, Рыба, Птица')],
            [KeyboardButton(text='Гарниры'),
            KeyboardButton(text='На Компанию')],
            [KeyboardButton(text='Десерты'),
            KeyboardButton(text='Хлеб и Выпечка')]
        ],
        # one_time_keyboard=True,
        # resize_keyboard=True
    )
    return kb



