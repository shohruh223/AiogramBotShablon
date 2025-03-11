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


def photo_inline():
    button = InlineKeyboardButton(text="Like 👍", callback_data="like")
    button2 = InlineKeyboardButton(text="Dislike 👎", callback_data="dislike")
    button3 = InlineKeyboardButton(text="Back ◀️", callback_data="back inline 2")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button3],
        ]
    )
    return ikm


def media_inline():
    button = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/hadichvvy/")
    button2 = InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/")
    button3 = InlineKeyboardButton(text="Telegram", url="https://t.me/@hadchvvy")
    button4 = InlineKeyboardButton(text="Back ◀️", callback_data="back inline 3")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2, button3],
            [button4],
        ]
    )
    return ikm