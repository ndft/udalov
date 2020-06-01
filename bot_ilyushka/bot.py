import telebot
import random

from telebot import types

bot = telebot.TeleBot('1130583146:AAG5vS_5BbgfaPI4_fLlqiXBs7vfocnDfdM')

@bot.message_handler(commands=['start'])
def start_message(message):
#    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Как дела?')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, '
                                      'бот созданный, чтобы повторять и бесить тебя'.format(message.from_user,
                                       bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Хорошо', callback_data='good')
            item2 = types.InlineKeyboardButton('Не очень', callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Норм, а твои?', reply_markup=markup)
        elif message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Привет, какашка')
        elif message.text.lower() == 'пока':
            bot.send_message(message.chat.id, 'Уже сбегаешь к мамочке?')
        elif message.text.lower() == 'ты илья?':
            bot.send_message(message.chat.id, 'сисественно')
        else:
            bot.send_message(message.chat.id, message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Рад за тебя')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Фигово тебе')
            # remove inline button
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?", reply_markup=None)
            # show alert
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='Это тестовое уведомление')
    except Exception as e:
        print(repr(e))
# RUN
bot.polling(none_stop=True)