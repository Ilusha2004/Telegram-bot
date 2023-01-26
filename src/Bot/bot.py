import telebot

bot = telebot.TeleBot('5875940701:AAGra5jHn_Kec4-dJYIGjLs3ItMcVy4sBqY')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    mes = f'Hello <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    # bot.send_message(message.chat.id, mes, parse_mode='html')
    bot.reply_to(message, "Howdy, how are you doing?")
    
# @bot.message_handler(func=lambda m: True)pip3 uninstall telebotp
# def echo_all(message):
# 	bot.reply_to(message, message.text)
 
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

# Which could also be defined as:
def test_message(message):
	return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	pass

# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
# @bot.message_handler(commands=['hello'])
# @bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
# def send_something(message):
#     pass


# bot.polling(non_stop=True)
bot.infinity_polling()