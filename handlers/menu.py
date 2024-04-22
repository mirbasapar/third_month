from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.menu_kb import menu_kb
from bot import database


menu_router = Router()


@menu_router.message(Command('menu'))
async def start_cmd(message: types.Message):
    await message.answer(f'Категорий меню:', reply_markup=menu_kb())


categories = ['Закуски', 'Салаты', 'Супы', 'Открытый огонь и Хоспер', 'Сезоны Кыргызстана', 
        'Мясо, Рыба, Птица', 'Гарниры', 'На Компанию', 'Десерты', 'Хлеб и Выпечка']


@menu_router.message(F.text.in_(categories))
async def show_menu(message: types.Message):
    category = message.text
    print(category)
    menu_kb = types.ReplyKeyboardRemove()
    data = await database.fetch(
        """
        SELECT f.* FROM menu m JOIN foods f 
        on m.id = f.menu_id WHERE m.name = ?
        """, 
        (category,), 
        fetch_type='all'
    )
    if not data:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=menu_kb())
    await message.answer(f'Категория меню - {category}:')
    for food in data:
        price = food['price']
        name = food['name']
        photo = types.FSInputFile(food['picture'])
        await message.answer_photo(
            photo=photo, 
            caption = f'{name}\n Цена: {price} сом. ')


# @menu_router.message(F.text.lower() == 'закуски')
# async def snacks(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Закуски: https://barashek.kg/product-category/zakuski/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'салаты')
# async def salat(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Салаты: https://barashek.kg/product-category/salaty/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'супы')
# async def soup(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Супы: https://barashek.kg/product-category/supy/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'открытый огонь и хоспер')
# async def fire(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Открытый огонь и Хоспер: https://barashek.kg/product-category/goryachee/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'сезоны кыргызстана')
# async def kg(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Сезоны Кыргызстана: https://barashek.kg/product-category/sezony-kyrgyzstana/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'мясо, рыба, птица')
# async def meat(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Мясо, Рыба, Птица: https://barashek.kg/product-category/myaso-ryba-ptitsa/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'гарниры')
# async def garnish(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Гарниры: https://barashek.kg/product-category/garniry/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'на компанию')
# async def comp(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("На Компанию: https://barashek.kg/product-category/na-kompaniyu/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'десерты')
# async def desert(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Десерты: https://barashek.kg/product-category/deserty/", reply_markup = kb)


# @menu_router.message(F.text.lower() == 'хлеб и выпечка')
# async def bread(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     await message.answer("Хлеб и Выпечка: https://barashek.kg/product-category/hleb-i-vypechka/", reply_markup = kb)
