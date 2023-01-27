# Тестируем эхо бота c обработкой запросов через методы диспетчера
# Импорт классов и модулей из aiogram
from aiogram import Bot, Dispatcher, executor, types


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = '5901014831:AAE4Kc2qrCFr1ER3snSbQvO1EAX0MYBil8A'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: types.Message):
await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: types.Message):
await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на отправку фото
async def send_photo_echo(message: types.Message):
await message.answer_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на отправку видео
async def send_video_echo(message: types.Message):
await message.answer_video(message.video.file_id)



# Этот хэндлер будет срабатывать на отправку видео сообщений
async def send_video_note_echo(message: types.Message):
await message.answer_video_note(message.video_note.file_id)


# Этот хэндлер будет срабатывать на отправку стикеров
async def send_sticker_echo(message: types.Message):
await message.answer_sticker(message.sticker.file_id)


# Этот хэндлер будет срабатывать на отправку аудио файлов
async def send_audio_echo(message: types.Message):
await message.answer_audio(message.audio.file_id)


# Этот хэндлер будет срабатывать на отправку голосовых сообщений
async def send_voice_echo(message: types.Message):
await message.answer_voice(message.voice.file_id)


# Этот хэндлер будет срабатывать на отправку любых файлов
async def send_files(message: types.Message):
await message.answer_document(message.document.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def send_echo(message: types.Message):
await message.reply(message.text)


# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_video_echo, content_types=['video'])
dp.register_message_handler(send_video_note_echo, content_types=['video_note'])
dp.register_message_handler(send_sticker_echo, content_types=['sticker'])
dp.register_message_handler(send_audio_echo, content_types=['audio'])
dp.register_message_handler(send_voice_echo, content_types=['voice'])
dp.register_message_handler(send_files,content_types=['document'])
dp.register_message_handler(send_echo)


if __name__ == '__main__':
executor.start_polling(dp, skip_updates=True)