from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    button = KeyboardButton(text="Kurs")
    button2 = KeyboardButton(text="Get Username")
    button3 = KeyboardButton(text="Wikipedia")
    button4 = KeyboardButton(text="Tarjimon bot")
    button5 = KeyboardButton(text="QR code bot")
    button6 = KeyboardButton(text="remove bg bot")
    button7 = KeyboardButton(text="echo bot")
    button8 = KeyboardButton(text="self my bot")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5, button6],
            [button7, button8],
        ],
        resize_keyboard=True
    )
    return rkm


def back_menu():
    button = KeyboardButton(text="⬅️ back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
        ],
        resize_keyboard=True
    )
    return rkm


def language_menu():
    button = KeyboardButton(text="🇺🇿 ➡️ 🇬🇧")
    button2 = KeyboardButton(text="🇬🇧 ➡️ 🇺🇿")
    button3 = KeyboardButton(text="⬅️ back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
        ],
        resize_keyboard=True
    )
    return rkm

def my():
    button = KeyboardButton(text="About me")
    button2 = KeyboardButton(text="Media url")
    button3 = KeyboardButton(text="Family")
    button4 = KeyboardButton(text="back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2, button3],
            [button4],
        ],
        resize_keyboard=True
    )
    return rkm
