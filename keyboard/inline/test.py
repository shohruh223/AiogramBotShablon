from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_main_menu():
    button = InlineKeyboardButton(text="Inline Keyboard 1", callback_data="keyboard_1")
    button2 = InlineKeyboardButton(text="Dostingizga ulashish", switch_inline_query="")
    button4 = InlineKeyboardButton(text="Ortga Alerntsiz", callback_data="back_1")
    button3 = InlineKeyboardButton(text="Ortga Alernt bilan", callback_data="back_2")
    button5 = InlineKeyboardButton(text="Url ochish", url="https://github.com/shohruh223/AiogramBoTutorialVersion2/")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button5],
            [button3, button4],
        ]
    )
    return ikm
