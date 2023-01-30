from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU


# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                     resize_keyboard=True)

button_yes: KeyboardButton = KeyboardButton(LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(LEXICON_RU['no_button'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
yes_no_kb.add(button_yes, button_no)


# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)

button_1: KeyboardButton = KeyboardButton(LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(LEXICON_RU['paper'])

# Располагаем кнопки в клавиатуре одну под другой в 3 ряда
game_kb.add(button_1).add(button_2).add(button_3)