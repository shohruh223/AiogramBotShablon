from aiogram import Router
from aiogram import types, F
from aiogram.filters import Command
from handler.users.dollar_test import kurs
from keyboard.default.default_keyboard import main_menu

router = Router()

@router.message(F.text == "Kurs")
async def send_start(message: types.Message):
    await message.answer(text=f"Bugungi dollar kursi {kurs}",
                         reply_markup=main_menu())







