from aiogram import Router, types


echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    # logging.info(message.text)
    await message.answer("Я не понимаю Вас, попробуйте следующие команды: "
                         "/start - начать диалог")