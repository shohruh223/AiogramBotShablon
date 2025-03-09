from aiogram import Router, F
from aiogram import types
from keyboard.default.main_keyboard import reply_keyboards

router = Router()


@router.message(F.text == "Reply Keyboard 1")
async def send_help(message: types.Message):
    await message.answer("Bu Reply Keyboard 1")


@router.message(F.text == "Reply Keyboard 2")
async def send_help(message: types.Message):
    await message.answer("Bu Reply Keyboard 2")


@router.message(F.text == "Ortga")
async def send_help(message: types.Message):
    await message.answer("Ortga", reply_markup=reply_keyboards())
