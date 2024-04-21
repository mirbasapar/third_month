from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types
import sqlite3
from bot import database


review_router = Router()
db = sqlite3.connect("db.sqlite")
cursor = db.cursor()


class BookSurvey(StatesGroup):
    name = State()
    contact = State()
    date_visit = State()
    food_quality = State()
    clean_est = State()
    add_comment = State()


@review_router.message(Command("stop_review"))
@review_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")


@review_router.message(Command('review'))
async def start_review(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer('Как вас зовут?')


@review_router.callback_query(F.data == 'review')
async def start_review(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookSurvey.name)
    await cb.message.answer('Как вас зовут?')


@review_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.contact)
    await state.update_data(name=message.text)
    await message.answer('Ваш номер телефона или Instagram: ')


@review_router.message(BookSurvey.contact)
async def process_contact(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.date_visit)
    await state.update_data(contact=message.text)
    await message.answer('Дата вашего посещения нашего заведения (введите в формате ГГГГММДД): ')


@review_router.message(BookSurvey.date_visit)
async def process_date(message: types.Message, state: FSMContext):
    date_visit = message.text
    if not date_visit.isdigit():
        await message.answer('Пожалуйста, введите число (в формате ГГГГММДД): ')
        return
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='плохо'),
                types.KeyboardButton(text='удовлетворительно')
            ],
            [    
                types.KeyboardButton(text='хорошо'),
                types.KeyboardButton(text='отлично')
            ]
        ], resize_keyboard=True
    )   
    await state.set_state(BookSurvey.food_quality)
    await state.update_data(date_visit=int(date_visit))
    await message.answer('Как оцениваете качество еды: ', reply_markup=kb)


@review_router.message(BookSurvey.food_quality)
async def process_food(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='было грязно'),
                types.KeyboardButton(text='затрудняюсь ответить')
            ],
            [    
                types.KeyboardButton(text='чисто'),
                types.KeyboardButton(text='уютно')
            ]
        ], resize_keyboard=True
    )
    await state.set_state(BookSurvey.clean_est)
    await state.update_data(food_quality=message.text)
    await message.answer('Как оцениваете чистоту заведения: ', reply_markup=kb)


@review_router.message(BookSurvey.clean_est)
async def process_comment(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.add_comment)
    await state.update_data(clean_est=message.text)
    data = await state.get_data()
    print("!", data)
    await message.answer('Дополнительные комментарии')


@review_router.message(BookSurvey.add_comment)
async def process_clean(message: types.Message, state: FSMContext):
    await state.update_data(add_comment=message.text)
    data = await state.get_data()
    print("~", data)
    await database.execute(
        "INSERT INTO review (name, contact, date_visit, food_quality, clean_est, add_comment) VALUES (?, ?, ?, ?, ?, ?)",
        (data['name'], data['contact'], data['date_visit'], data['food_quality'], data['clean_est'], data['add_comment'])
    )
    await message.answer('Мы отправили ваш отзыв!')
    await state.clear()