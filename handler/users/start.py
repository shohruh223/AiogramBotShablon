from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from keyboard.default_keyboard import main_menu

router = Router()


@router.message(Command("start"))
async def send_start(message: types.Message):
    await message.answer(text="Salom, bu 9-modul uchun yakuniy\n"
                              "imtihon loyihasi boti",
                         reply_markup=main_menu())






    
