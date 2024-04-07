from aiogram.filters import Command
from aiogram import Router, types, F


callback_router = Router()

@callback_router.callback_query(F.data == 'adress')
async def adress(callback: types.CallbackQuery):
    await callback.message.answer(text = 'Наш адрес: г. Бишкек, ул. Токомбаева, 78')

@callback_router.callback_query(F.data == 'contact')
async def contact(callback: types.CallbackQuery):
    await callback.message.answer(text = 'Телефон: +996 (312) 52-11-11\n' 'Моб.тел.: +996 (556) 52-11-11\n' 'E-mail: barashek@kaynar.kg')    