# import requests
# BASE_URL = 'https://api.telegram.org/bot1238482310:AAGcXRIZ7Pz0QOUhPJV7aBFu7q0o8r270CQ/'
# r = requests.get(f'{BASE_URL}getMe')
# print(r)
# print(r.json())
# r = requests.get(f'{BASE_URL}getUpdates')
# print(r.json())
#
# import pprint
# pprint.pprint(r.json())
# print(r.json())

import telebot
from telebot.types import Message

TOKEN = '1238482310:AAGcXRIZ7Pz0QOUhPJV7aBFu7q0o8r270CQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Приветы-котлеты')

@bot.message_handler(func=lambda message: True)
def any_message(message: Message):
    bot.reply_to(message, message.text.upper())

bot.polling()

