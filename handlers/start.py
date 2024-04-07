from aiogram.filters import Command
from aiogram import Router, types
from keyboards.start_kb import start_kb


start_router = Router()

@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет! {message.from_user.first_name}', reply_markup=start_kb())


@start_router.message(Command('myinfo'))
async def send_myinfo(message: types.Message):
    await message.answer(f"Your ID: {message.from_user.id}\n"
                         f"Your first name: {message.from_user.first_name}\n"
                         f"Your nic name: {message.from_user.username}")
