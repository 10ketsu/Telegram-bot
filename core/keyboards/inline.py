from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

ikb_site = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Открыть', web_app=WebAppInfo(url=f'https://admissions.kpfu.ru/prozhivanie/obshhezhitiya/'))
                                    ]
                                ])
