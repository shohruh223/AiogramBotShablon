import asyncio
import wikipedia
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from keyboard.default.default_keyboard import main_menu, back_menu
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from states.wikipwdiya import GetUsernameState2

router = Router()


wikipedia.set_lang("uz")


@router.message(F.text == "Wikipedia")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Sizga nima haqida ma'lumot kerak",
                         reply_markup=back_menu())
    await state.set_state(GetUsernameState2.data)

@router.message(StateFilter(GetUsernameState2.data))
async def echo(message: types.Message, state: FSMContext):
    data = wikipedia.summary(message.text)
    await message.answer(data)

    await state.set_state(GetUsernameState2.data)


@router.message(StateFilter("*"), F.text == "⬅️ back")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text="Ortga",
                         reply_markup=main_menu())
    await state.clear()

