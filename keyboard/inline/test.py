from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def about_me_inline():
    button = InlineKeyboardButton(text="Fullname", callback_data="fullname")
    button2 = InlineKeyboardButton(text="Photo", callback_data="photo")
    button3 = InlineKeyboardButton(text="Job", callback_data="job")
    button4 = InlineKeyboardButton(text="Back ◀️", callback_data="back inline 1")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2, button3],
            [button4],
        ]
    )
    return ikm