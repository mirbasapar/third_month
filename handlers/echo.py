from aiogram import Router, types
from bot import bot
import logging
from aiogram.types import ReplyKeyboardRemove

echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    logging.info(message.text)
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())