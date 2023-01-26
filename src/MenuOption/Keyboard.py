import telebot
from telebot import types

TOKEN = '5875940701:AAGra5jHn_Kec4-dJYIGjLs3ItMcVy4sBqY'

bot = telebot.TeleBot(TOKEN)

markup_1 = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup_1.add(itembtn1, itembtn2, itembtn3)

@bot.message_handler(commands=['test'])
def markup(message):
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup_1)

# or add KeyboardButton one row at a time:
markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)

@bot.message_handler(commands=['hello'])
def fuck(message):
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

bot.infinity_polling()