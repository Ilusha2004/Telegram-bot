from aiogram import Bot, Dispatcher
from aiogram.types import Message

async def get_photo(message: Message):
    with open("resources/image.jpeg", 'wr+') as file1:
        file1 = message.photo[0].file_id
        print(file1)
    await message.reply_photo(message.photo[0].file_id)

# async def send_photo(message: Message):

def initial(dp: Dispatcher):
    dp.register_message_handler(get_photo, commands=["/photo"])