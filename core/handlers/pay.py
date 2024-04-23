from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Оплата за проживание в общежитии',
        description='Деревня универсиада',
        payload ='Payment through a bot',
        provider_token='***',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Найм обучающегося',
                amount=90000
            ),
            LabeledPrice(
                label='Электричество',
                amount=1000
            )
        ],
        photo_url='https://vlfin.ru/uploads/bGCpLxAxiL2pwKnFsb8sfM2yxZWPZrrqYJb52MS2.jpg',
        photo_width=800,
        photo_height=600,
        need_email=True,
        need_phone_number=True,
        send_email_to_provider=True,
        protect_content=True
    )


async def order2(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Оплата за проживание в общежитии',
        description='Общежитие №9',
        payload ='Payment through a bot',
        provider_token='***',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Найм обучающегося',
                amount=75000
            ),
            LabeledPrice(
                label='Электричество',
                amount=1000
            )
        ],
        photo_url='https://students.kpfu.ru/sites/default/files/inline-images/DSC_0968.JPG',
        photo_width=800,
        photo_height=600,
        need_email=True,
        need_phone_number=True,
        send_email_to_provider=True,
        protect_content=True
    )


async def order3(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Оплата за проживание в общежитии',
        description='Красная позиция',
        payload ='Payment through a bot',
        provider_token='***',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Найм обучающегося',
                amount=15000
            ),
            LabeledPrice(
                label='Электричество',
                amount=1000
            )
        ],
        photo_url='https://students.kpfu.ru/sites/default/files/inline-images/1_1.JPG',
        photo_width=800,
        photo_height=600,
        need_email=True,
        need_phone_number=True,
        send_email_to_provider=True,
        protect_content=True
    )



async def pre_checkout_query(pre_checkout_query:PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successful_payment(message: Message):
   msg = f'Оплата от пользователя: {message.from_user.first_name} \nна сумму: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} \nПрошла успешно'
   await message.answer(msg)
