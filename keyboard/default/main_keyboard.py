from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu():
    button = KeyboardButton(text="Reply Keyboard 1")
    button2 = KeyboardButton(text="Reply Keyboard 2")
    button3 = KeyboardButton(text="Lakatsiya ulashish", request_location=True)
    button4 = KeyboardButton(text="Telefon raqamni ulashish", request_contact=True)
    button5 = KeyboardButton(text="Ortga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm


def reply_keyboards():
    button = KeyboardButton(text="Reply Keyboard")
    button1 = KeyboardButton(text="Inline Keyboard")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button1],
        ],
        resize_keyboard=True
    )
    return rkm
