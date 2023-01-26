import telebot

TOKEN = '5875940701:AAGra5jHn_Kec4-dJYIGjLs3ItMcVy4sBqY'
bot = telebot.TeleBot(TOKEN)
Regex = '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+'

class TestBot: 
    
    def __init__(self) -> None:
        pass
    
    def start(self):
        pass
    
@bot.message_handler(commands=['start', 'help'])
def start(message):
    mes = f'Hello <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    # bot.send_message(message.chat.id, mes, parse_mode='html')
    bot.reply_to(message, "Howdy, how are you doing?")
        
if __name__ == '__main__':
    print(Parser.reversed_polish_notation("2.0 - 3.5 + 6"))

bot.infinity_polling()
    