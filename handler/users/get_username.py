from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from keyboard.default.default_keyboard import main_menu, back_menu
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from states.main import GetUsernameState

router = Router()


@router.message(F.text == "Get Username")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Username link qaytaradi, telefon raqam kiriting",
                         reply_markup=back_menu())
    await state.set_state(GetUsernameState.confirm)


@router.message(StateFilter("*"), F.text == "⬅️ back")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text="Ortga",
                         reply_markup=main_menu())
    await state.clear()


@router.message(StateFilter(GetUsernameState.confirm), F.text.startswith("+998"))
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"https://t.me/{message.text}")
    await state.set_state(GetUsernameState.confirm)




