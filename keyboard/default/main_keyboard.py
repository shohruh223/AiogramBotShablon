from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def contact_menu():
    button = KeyboardButton(text="Contact", request_contact=True)
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]],
        resize_keyboard=True)
    return rkm


def location_menu():
    button = KeyboardButton(text="Location", request_location=True)
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]],
        resize_keyboard=True)
    return rkm
