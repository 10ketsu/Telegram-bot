from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Оплата',
        description='Описание',
        payload ='Payment through a bot',
        provider_token='381764678:TEST:83120',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Оплата ДУ',
                amount=15000
            )
        ],
        photo_url='https://sun9-10.userapi.com/impg/3EpunYie8lnDEYIm4xAC_R7ft43Qv-4hDMT-_A/D8L_W5tpfyg.jpg?size=432x320&quality=96&sign=b964d15b32a4e1dc9ae92685f6f2f8fe&type=album',
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
