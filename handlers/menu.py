from aiogram.filters import Command
from aiogram import Router, types, F
from keyboards.menu_kb import menu_kb


menu_router = Router()

@menu_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    await callback.message.answer(text = 'Меню', reply_markup=menu_kb())
   