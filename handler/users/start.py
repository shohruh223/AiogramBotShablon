from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command

from keyboard.default.main_keyboard import main_menu, reply_keyboards
from keyboard.inline.test import inline_main_menu

router = Router()


@router.message(Command("start"))
async def send_start(message: types.Message):
    await message.answer("Salom bu Shohruh Abdurahmon tomonidan yaratilgan bot shablon!\n"
                         "Mualliflik huquqi bor shu sababli foydalanishdan oldin\n"
                         "meni duo qilib ishlating, aks holda rozi emasman!", reply_markup=reply_keyboards())


@router.message(F.text == "Reply Keyboard")
async def send_help(message: types.Message):
    await message.answer("Bu Replay Keyboard'lar", reply_markup=main_menu())


@router.message(F.text == "Inline Keyboard")
async def send_help(message: types.Message):
    await message.answer("Bu Inline Keyboard'lar", reply_markup=inline_main_menu())
