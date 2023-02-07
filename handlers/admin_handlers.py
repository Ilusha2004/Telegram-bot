from aiogram import Bot, Dispatcher
from aiogram.types import Message

async def get_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

def initial(dp: Dispatcher):
    dp.register_message_handler(get_photo)