from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
async def set_commands (bot: Bot) :
    commands = [

        BotCommand (
            command= 'cancel',
            description= 'Сбросить'
        ),
        BotCommand (
            command='pay',
            description='оплата'
        ),
]

    await bot. set_my_commands(commands, BotCommandScopeDefault)
