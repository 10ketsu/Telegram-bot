from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Оплата',
        description='Описание',
        payload ='Payment through a bot',
        provider_token='***',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Оплата ДУ',
                amount=15000
            )
        ],
        photo_url='***',
        photo_width=800,
        photo_height=600,
        need_email=True,
        need_phone_number=True,
        send_email_to_provider=True
    )



async def pre_checkout_query(pre_checkout_query:PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successful_payment(message: Message):
   msg = f'Спасибо, оплата прошла успешно {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'
   await message.answer(msg)
