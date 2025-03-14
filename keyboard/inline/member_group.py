from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import GROUP_USERNAME


def subscribe_ikm():
    button = InlineKeyboardButton(text="Guruhga obuna bo'lish", url=f"https://t.me/{GROUP_USERNAME.strip('@')}")
    button2 = InlineKeyboardButton(text="Tekshirsh☑️", callback_data="tekshirsh")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button],
            [button2]
        ])

    return ikm
