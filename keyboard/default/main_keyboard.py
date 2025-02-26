from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    button = KeyboardButton(text="🏢 Kompaniya haqida")
    button2 = KeyboardButton(text="📍 Fililallar")
    button3 = KeyboardButton(text="💼 Bo'sh ish o'rinlari")
    button4 = KeyboardButton(text="Menyu")
    button5 = KeyboardButton(text="🗣 Yangiliklar")
    button6 = KeyboardButton(text="📞 Kontaktlar/Manzil")
    button7 = KeyboardButton(text="🇺🇿/🇷🇺 Til")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button4, button5],
            [button6, button7],
        ],
        resize_keyboard=True
    )
    return rkm