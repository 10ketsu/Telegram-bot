from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Документы для заселения'
        ),
        KeyboardButton(
            text='text'

        )
    ],

    [
        KeyboardButton(
            text='Универсиада'
        ),
        KeyboardButton(
            text='Пушка'
        ),
        KeyboardButton(
            text='Красная позиция'
        )

    ]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку ⬇️')
