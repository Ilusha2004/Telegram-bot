# import telebot
# from telebot.async_telebot import AsyncTeleBot

# bot = AsyncTeleBot('5875940701:AAGra5jHn_Kec4-dJYIGjLs3ItMcVy4sBqY')

# @bot.message_handler(content_types=['photo'])
# async def new_message(message: telebot.types.Message):
#     result_message = await bot.send_message(message.chat.id, '<i>Downloading your photo...</i>', parse_mode='HTML', disable_web_page_preview=True)
#     file_path = await bot.get_file(message.photo[-1].file_id)
#     downloaded_file = await bot.download_file(file_path.file_path)
#     with open('resource/test.jpeg', 'wb') as new_file:
#         new_file.write(downloaded_file)
#     await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Done!</i>', parse_mode='HTML')

# import asyncio
# asyncio.run(bot.polling())