from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, ContentType
import asyncio
from aiogram.filters import Command, CommandStart
from core.handlers.basic import get_DU, get_start, get_DUINFO, get_back
from core.settings import settings
from core.handlers.pay import order, pre_checkout_query, successful_payment
from core.utils.commands import set_commands
from aiogram import F


async def start():
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.message.register(get_start, F.text == '/start')
    dp.message.register(get_DU, F.text == 'Универсиада')
    dp.message.register(get_DUINFO, F.text == 'Информация ДУ')
    dp.message.register(order, F.text == 'Оплата ДУ')
    dp.message.register(get_back, F.text == 'Назад')
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
    #dp.message(F.successful_payment)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
