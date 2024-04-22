import asyncio
from aiogram import Bot
import logging
from bot import bot, dp, set_my_menu, database
from handlers import start_router, pic_router, menu_router, review_router, echo_router


async def on_startup(bot: Bot):
    await database.create_tables()


async def main():
    await set_my_menu()
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(review_router)
    dp.include_router(menu_router)
#в конце
    dp.include_router(echo_router)
#запуск бота
    dp.startup.register(on_startup)
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

