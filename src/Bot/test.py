from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('5875940701:AAGra5jHn_Kec4-dJYIGjLs3ItMcVy4sBqY')

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
	await bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
async def echo_all(message):
	await bot.reply_to(message, message.text)


import asyncio
asyncio.run(bot.polling(skip_pending=True)) # to skip updates