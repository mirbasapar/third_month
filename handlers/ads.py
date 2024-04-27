from aiogram import Router, types, F
from aiogram.filters import Command
from crawler.house_kg import HouseCrawler


ads_router = Router()


@ads_router.message(Command("get_ads"))
async def get_ads(message: types.Message):
    crawler = HouseCrawler()
    house_links = await crawler.get_houses()
    for link in house_links:
        await message.answer(link, parse_mode="HTML")
