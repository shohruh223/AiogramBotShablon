from aiogram import Router, F
from aiogram import types
from keyboard.default.main_keyboard import reply_keyboards

router = Router()


@router.callback_query(F.data == "keyboard_1")
async def send_help(callback: types.CallbackQuery):
    await callback.message.answer("Bu Inline Keyboard 1")


@router.callback_query(F.data == "back_1")
async def send_help(callback: types.CallbackQuery):
    await callback.answer("Ortga", reply_markup=reply_keyboards())

@router.callback_query(F.data == "back_2")
async def send_help(callback: types.CallbackQuery):
    await callback.answer("Ortga", show_alert=True, reply_markup=reply_keyboards())
