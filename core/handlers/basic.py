from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!',
                           reply_markup=reply_keyboard)


async def get_DU(message: Message, bot:Bot):
    await bot.send_message(message.from_user.id, f'Общежитие деревни Универсиады в городе Казани – это современное жилое здание, специально построенное для проживания участников и гостей мирового спортивного события. Оно стало настоящим центром жизни и общения во время Универсиады \n'
                                                                              'Общежитие предлагает комфортабельные номера различных категорий – от одноместных до многокомнатных. В каждом номере есть все необходимое для удобного проживания: удобная мебель, современные бытовые приборы, санузлы и душевые.',
    reply_markup = reply_keyboard)
