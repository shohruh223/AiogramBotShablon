from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio
from keyboard.default.default_keyboard import main_menu, back_menu
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from states.main import my1
from aiogram.types import ReplyKeyboardRemove
from keyboard.default.default_keyboard import my
from keyboard.inline.inline_keyboard import media_inline
router = Router()

@router.message(F.text == "self my bot")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Sizga nima haqida ma'lumot kerak",
                         reply_markup=my())
    await state.set_state(my1.data)


@router.message(F.text == "About me")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Mani ismim Hadicha Abduvosiqova.\n"
                              f" Yoshim 15 da. 9 sinfda o'qiyman.",
                         reply_markup=my())
    await state.set_state(my1.data)


@router.message(F.text == "Media url")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Men haqimda",
                         reply_markup=media_inline())
    await state.set_state(my1.data)

@router.message(F.text == "back")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Orqaga",
                         reply_markup=main_menu())
    await state.set_state(my1.data)



@router.message(F.text == "Family")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Bizani oila 5 kishidan iborat.\n"
                              f"Adam , oyim, opam, ukam, man.",
                         reply_markup=my())
    await state.set_state(my1.data)