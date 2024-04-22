from aiogram import Router, types, F
from aiogram.filters import Command
from crawler.house_kg import HouseCrawler


ads_router = Router()


@ads_router.message(Command("get_ads"))
async def get_ads(message: types.Message):
    crawler = HouseCrawler()
    crawler.get_page()
    house_links = crawler.get_house_links()
    for link in house_links:
        await message.answer(link, parse_mode="HTML")
