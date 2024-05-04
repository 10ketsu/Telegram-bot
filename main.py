from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, ContentType, FSInputFile
import asyncio
from aiogram.filters import Command, CommandStart
from core.handlers.basic import get_start, get_back, get_document, get_site
from core.handlers.basic import get_DU, get_DUINFO, get_PU, get_PUINFO, get_KP, get_KPINFO
from core.settings import settings
from core.handlers.pay import order, pre_checkout_query, successful_payment, order2, order3
from core.utils.commands import set_commands
from aiogram import F


async def start():
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()

    dp.message.register(get_start, F.text == '/start')
    dp.message.register(get_site, F.text == '/site')
    dp.message.register(get_document, F.text == 'Документы для заселения')
    dp.message.register(get_DU, F.text == 'Универсиада')
    dp.message.register(get_DUINFO, F.text == 'Информация ДУ')
    dp.message.register(order, F.text == 'Оплата ДУ')
    dp.message.register(get_PU, F.text == 'Пушка')
    dp.message.register(get_PUINFO, F.text == 'Информация Пушка')
    dp.message.register(order2, F.text == 'Оплата Пушка')
    dp.message.register(get_KP, F.text == 'Красная позиция')
    dp.message.register(get_KPINFO, F.text == 'Информация Красная позиция')
    dp.message.register(order3, F.text == 'Оплата Красная позиция')
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
