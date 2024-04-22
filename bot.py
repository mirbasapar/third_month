from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from db.database import Database


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
database = Database(
    Path(__file__).parent / "db.sqlite"
)


async def set_my_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="myinfo", description="Мое инфо"),
        types.BotCommand(command="menu", description="Меню"),
        types.BotCommand(command="review", description="Оставить Отзыв", callback_data="review"),
        types.BotCommand(command="stop_review", description="Остановить Отзыв"),
        types.BotCommand(command="get_ads", description="Получить объявления с сайта house.kg")
    ])