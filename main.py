import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random


load_dotenv
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

#handlers

@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Hello!, {message.from_user.first_name}')

@dp.message(Command('myinfo'))
async def send_myinfo(message: types.Message):
    await message.answer(f"Your ID: {message.from_user.id}\n"
                         f"Your first name: {message.from_user.first_name}\n"
                         f"Your nic name: {message.from_user.username}")
    
@dp.message(Command('picture'))
async def send_random_pic(message: types.Message):
    images_dir = 'images'
    image_files = types.FSInputFile(random(images_dir))
    await message.answer_photo(photo=image_files)


# @dp.message(Command('picture'))
# async def send_picture(message: types.Message):
#     file = types.FSInputFile('images/python.jpeg')
#     await message.answer_photo(photo=file)

@dp.message()
async def echo(message: types.Message):
    logging.info(message.text)
    await message.answer(message.text)

async def main():
    # start bot
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
