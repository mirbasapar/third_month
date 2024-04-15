from aiogram import Router, types, F
from keyboards.menu_kb import menu_kb


menu_router = Router()


@menu_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    await callback.message.answer(text = 'Категорий меню:', reply_markup=menu_kb())


@menu_router.message(F.text.lower() == 'закуски')
async def snacks(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Закуски: https://barashek.kg/product-category/zakuski/")


@menu_router.message(F.text.lower() == 'салаты')
async def salat(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Салаты: https://barashek.kg/product-category/salaty/")


@menu_router.message(F.text.lower() == 'супы')
async def soup(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Супы: https://barashek.kg/product-category/supy/")


@menu_router.message(F.text.lower() == 'открытый огонь и хоспер')
async def fire(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Открытый огонь и Хоспер: https://barashek.kg/product-category/goryachee/")


@menu_router.message(F.text.lower() == 'сезоны кыргызстана')
async def kg(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Сезоны Кыргызстана: https://barashek.kg/product-category/sezony-kyrgyzstana/")


@menu_router.message(F.text.lower() == 'мясо, рыба, птица')
async def meat(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Мясо, Рыба, Птица: https://barashek.kg/product-category/myaso-ryba-ptitsa/")


@menu_router.message(F.text.lower() == 'гарниры')
async def garnish(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Гарниры: https://barashek.kg/product-category/garniry/")


@menu_router.message(F.text.lower() == 'на компанию')
async def comp(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("На Компанию: https://barashek.kg/product-category/na-kompaniyu/")


@menu_router.message(F.text.lower() == 'десерты')
async def desert(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Десерты: https://barashek.kg/product-category/deserty/")


@menu_router.message(F.text.lower() == 'хлеб и выпечка')
async def bread(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Хлеб и Выпечка: https://barashek.kg/product-category/hleb-i-vypechka/")