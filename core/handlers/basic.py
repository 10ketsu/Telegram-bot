from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
import json
from core.keyboards.reply import reply_keyboard, reply_keyboard2, reply_keyboard3, reply_keyboard4
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.keyboards.inline import ikb_site



async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!',
                           reply_markup=reply_keyboard)



async def get_DU(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите интересующее',
                           reply_markup=reply_keyboard2)


#async def get_DUINFO(message: Message, bot: Bot):
#    await bot.send_photo(message.from_user.id, photo='https://kpfu.ru/portal/docs/F1672697176/IMG_1767.jpg', caption='Общежитие деревни Универсиады в городе Казани – это современное жилое здание, специально построенное для проживания участников и гостей мирового спортивного события. Оно стало настоящим центром жизни и общения во время Универсиады \n'
#                           'Общежитие предлагает комфортабельные номера различных категорий – от одноместных до многокомнатных. В каждом номере есть все необходимое для удобного проживания: удобная мебель, современные бытовые приборы, санузлы и душевые.',
#                           reply_markup=reply_keyboard2)

#async def get_DUINFO(message: Message, bot: Bot) :
#    photo = FSInputFile(path=r'C:\Users\Bogdan\Desktop\i.webp')
#    await bot. send_photo(message.chat.id, photo=photo, caption='Общежитие деревни Универсиады в городе Казани – это современное жилое здание, специально построенное для проживания участников и гостей мирового спортивного события. Оно стало настоящим центром жизни и общения во время Универсиады \n'
#                           'Общежитие предлагает комфортабельные номера различных категорий – от одноместных до многокомнатных. В каждом номере есть все необходимое для удобного проживания: удобная мебель, современные бытовые приборы, санузлы и душевые.',
#                             reply_markup=reply_keyboard2)

async def get_DUINFO(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\Bogdan\PycharmProjects\TG-bot\DU-sunny.webp'),
                                caption='Общежитие деревни Универсиады в городе Казани – это современное жилое здание, специально построенное для проживания участников и гостей мирового спортивного события. Оно стало настоящим центром жизни и общения во время Универсиады \n'
                                        'Общежитие предлагает комфортабельные номера различных категорий – от одноместных до многокомнатных. В каждом номере есть все необходимое для удобного проживания: удобная мебель, современные бытовые приборы, санузлы и душевые.',
                                reply_markup=reply_keyboard2)
    photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\Bogdan\PycharmProjects\TG-bot\DU_inside.jpg'))
    media = [photo1_mg, photo2_mg]
    await bot.send_media_group(message.chat.id, media)


async def get_PU(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите интересующее',
                           reply_markup=reply_keyboard3)



async def get_PUINFO(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\Bogdan\PycharmProjects\TG-bot\PU_outside.jpg'),
                                caption='Удобное расположение Общежитие №9 расположено на одной из главных улиц города Казани — ул. Пушкина,32. Это не помеха для твоего покоя и тишины, потому что дом находится в некотором отдалении от шумной магистрали. \n'
                                        'Зато все необходимые тебе объекты: СК УНИКС, Центр информационных технологий КФУ и сам университет в 5 минутах ходьбы. До центра города тоже рукой подать, так что вопрос, куда сходить, отпадает.',
                                reply_markup=reply_keyboard3)
    photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\Bogdan\PycharmProjects\TG-bot\PU_inside.jpg'))
    media = [photo1_mg, photo2_mg]
    await bot.send_media_group(message.chat.id, media)



async def get_KP(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите интересующее',
                           reply_markup=reply_keyboard4)




async def get_KPINFO(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\Bogdan\PycharmProjects\TG-bot\KP_outside.jpg'),
                                caption='Если ты приехал учиться в Казанский университет из другого города, заботливые родители могут снять для тебя квартиру. Но куда интереснее и дешевле жить в студенческом городке, в общежитии №4. \n'
                                        'Общая кухня, где так весело всем блоком готовить последнюю пачку пельменей и ждать стипендии. Общие праздники - без дорогих подарков, но с дорогими людьми и безумным весельем. Хочешь узнать, что такое студенческая романтика?',
                                reply_markup=reply_keyboard4)
    photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\Bogdan\PycharmProjects\TG-bot\KP_inside.jpg'))
    media = [photo1_mg, photo2_mg]
    await bot.send_media_group(message.chat.id, media)



async def get_document(message: Message, bot: Bot) :
    document = FSInputFile(path=r'C:\Users\Bogdan\PycharmProjects\TG-bot\sample1.pdf')
    await bot. send_document(message.chat.id, document=document, caption='Бланк для заселения')



async def get_site (message: Message, bot: Bot) :
    await bot.send_message(message.from_user.id, f'Сайт КФУ для абитуриентов',
                           reply_markup=ikb_site)



async def get_back(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Возврат на главную',
                           reply_markup=reply_keyboard)

