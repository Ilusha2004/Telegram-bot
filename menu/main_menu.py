from aiogram import Dispatcher
from aiogram.types import BotCommand
from lexicon.lexicon_ru import LEXICON_COMMANDS_RU

# Создаем асинхронную функцию
async def set_main_menu(dp: Dispatcher):
    # Создаем список с командами для кнопки menu
    main_menu_commands = [BotCommand(
                                command=command,
                                description=description
                          ) for command,
                                description in LEXICON_COMMANDS_RU.items()]

    print('processing')

    await dp.bot.set_my_commands(main_menu_commands)
