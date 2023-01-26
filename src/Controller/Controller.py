import telebot
import types
import logging
from telebot.async_telebot import AsyncTeleBot
from telebot import custom_filters

TOKEN = '5875940701:AAGra5jHn_Kec4-dJYIGjLs3ItMcVy4sBqY'

bot = AsyncTeleBot(TOKEN)
    
@bot.message_handler(commands=['start', 'help'])
async def start(message: telebot.types.Message):
    mes = f'Hello <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    await bot.send_message(message.chat.id, mes, parse_mode="HTML")
    
@bot.message_handler(content_types=['photo'])
async def new_message(message: telebot.types.Message):
    result_message = await bot.send_message(message.chat.id, '<i>Downloading your photo...</i>', parse_mode='HTML', disable_web_page_preview=True)
    file_path = await bot.get_file(message.photo[-1].file_id)
    downloaded_file = await bot.download_file(file_path.file_path)
    with open('resource/test.jpeg', 'wb') as new_file:
        new_file.write(downloaded_file)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Done!</i>', parse_mode='HTML')
    
@bot.message_handler(commands=['download'])
async def download_file(message: telebot.types.Message):
    file = open('resource/test.jpeg', 'rb')
    await bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(file)])
    file.close()

@bot.message_handler(commands=['document'])
async def document_send(message: telebot.types.Message):
    with open('test.docx', 'rb') as new_file:
        await bot.send_document(message.chat.id, new_file)

@bot.message_handler(commands=['photos'])
async def photos_send(message: telebot.types.Message):
    with open('resource/ker.jpeg', 'rb') as new_file, open('resource/ker.jpeg', 'rb') as new_file2:
        await bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(new_file), telebot.types.InputMediaPhoto(new_file2)])
        
@bot.channel_post_handler(func=lambda message: True)
async def doSmth(message: telebot.types.Message):
    await bot.send_message(message.chat.id, "govno")
    
@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)
        
###############################################################################################################################
        
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    # Class will check whether the user is admin or creator in group or not
    key='is_chat_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']
	
# # Now, you can use it in handler.
# @bot.message_handler(is_chat_admin=True)
# async def admin_of_group(message: telebot.types.Message):
# 	await bot.send_message(message.chat.id, 'You are admin of this group!')
 
@bot.message_handler(is_chat_admin=True, commands=['status'])
async def getStatus(message: telebot.types.Message):
    await bot.send_message(message.chat.id, 'You are admin of this group!')
    
@bot.message_handler(chat_id=[1876476172], commands=['admin']) # chat_id checks id corresponds to your list or not.
async def admin_rep(message):
    await bot.send_message(message.chat.id, "You are allowed to use this command.")

@bot.message_handler(commands=['admin'])
async def not_admin(message):
    print(message.chat.id)
    await bot.send_message(message.chat.id, "You are not allowed to use this command")
 
###############################################################################################################################

# if __name__ == '__main__':
    # To register filter, you need to use method add_custom_filter.
    
logger = telebot.logger
logger.logger.setLevel(logging.DEBUG)
    
bot.add_custom_filter(custom_filters.ChatFilter())
bot.add_custom_filter(IsAdmin())
import asyncio
asyncio.run(bot.polling())
    