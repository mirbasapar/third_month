from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.start_kb import start_kb
from keyboards.menu_kb import menu_kb

start_router = Router()


@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}!\n'
                         f'Добро пожаловать в ресторан "Барашек".', reply_markup=start_kb())


@start_router.message(Command('myinfo'))
async def send_myinfo(message: types.Message):
    await message.answer(f"Your ID: {message.from_user.id}\n"
                         f"Your first name: {message.from_user.first_name}\n"
                         f"Your nic name: {message.from_user.username}")


@start_router.callback_query(F.data == 'adress')
async def adress(callback: types.CallbackQuery):
    await callback.message.answer(text = 'Наш адрес: г. Бишкек, ул. Токомбаева, 78')


@start_router.callback_query(F.data == 'contact')
async def contact(callback: types.CallbackQuery):
    await callback.message.answer(text = 'Телефон: +996 (312) 52-11-11\n' 'Моб.тел.: +996 (556) 52-11-11\n' 'E-mail: barashek@kaynar.kg')


@start_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardRemove()
    await callback.message.answer(text = 'Категорий меню:', reply_markup=menu_kb())
