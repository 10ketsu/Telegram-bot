from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Документы для заселения'
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


reply_keyboard2 = ReplyKeyboardMarkup(keyboard = [
    [
        KeyboardButton(
            text='Информация ДУ'
        ),
        KeyboardButton(
            text='Оплата ДУ'
        ),
        KeyboardButton(
            text='Назад'
        )
    ]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку ⬇️')

reply_keyboard3 = ReplyKeyboardMarkup(keyboard = [
    [
        KeyboardButton(
            text='Информация Пушка'
        ),
        KeyboardButton(
            text='Оплата Пушка'
        ),
        KeyboardButton(
            text='Назад'
        )
    ]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку ⬇️')

reply_keyboard4 = ReplyKeyboardMarkup(keyboard = [
    [
        KeyboardButton(
            text='Информация Красная позиция'
        ),
        KeyboardButton(
            text='Оплата Красная позиция'
        ),
        KeyboardButton(
            text='Назад'
        )
    ]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку ⬇️')
