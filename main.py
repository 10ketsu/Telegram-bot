import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('35493713:AAH3RUT-GlPC7ohx1WNzTItC5E4A9cRpsAo')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://admissions.kpfu.ru/prozhivanie/obshhezhitiya/')

@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Универсиада', 'Пушка', 'Красная позиция', 'Documents']])
    bot.send_message(m.chat.id, 'Выберите интересующее', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'Универсиада':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Информация о ДУ', 'Оплата ДУ']])
        bot.send_message(message.chat.id, 'Выберите интересующее', reply_markup=keyboardgostart)
    elif message.text == 'Пушка':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Информация о Пушке', 'Оплата Пушка']])
        bot.send_message(message.chat.id, 'Выберите интересующее', reply_markup=keyboardgostart)
    elif message.text == 'Красаня позиция':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Информация о Красной позиции', 'Оплата Красная позиция']])
        bot.send_message(message.chat.id, 'Выберите интересующее', reply_markup=keyboardgostart)
    elif message.text == "Documents":
        bot.send_document(message.chat.id, document=open('sample1.pdf', 'rb'))

    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Информация о ДУ':
        bot.send_message(message.chat.id, 'Вот она')
        bot.send_photo(message.chat.id, photo=open('XXL.webp', 'rb'), caption='Общежитие деревни Универсиады в городе Казани – это современное жилое здание, специально построенное для проживания участников и гостей мирового спортивного события. Оно стало настоящим центром жизни и общения во время Универсиады \n'
                                                                              'Общежитие предлагает комфортабельные номера различных категорий – от одноместных до многокомнатных. В каждом номере есть все необходимое для удобного проживания: удобная мебель, современные бытовые приборы, санузлы и душевые. ')



@bot.message_handler(commands=['start'])
def site(message):
    bot.send_message(message.chat.id, '/start')



bot.polling(none_stop=True)