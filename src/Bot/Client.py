import telebot
from telebot import custom_filters

TOKEN: str = '5875940701:AAGra5jHn_Kec4-dJYIGjLs3ItMcVy4sBqY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(chat_id=[1876476172], commands=['admin']) # chat_id checks id corresponds to your list or not.
def admin_rep(message):
    bot.send_message(message.chat.id, "You are allowed to use this command.")

@bot.message_handler(commands=['admin'])
def not_admin(message):
    bot.send_message(message.chat.id, "You are not allowed to use this command")

# Do not forget to register
bot.add_custom_filter(custom_filters.ChatFilter())

bot.infinity_polling()