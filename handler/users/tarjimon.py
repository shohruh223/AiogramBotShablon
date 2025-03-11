from aiogram import types, F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from googletrans import Translator
from keyboard.default.default_keyboard import language_menu
from states.main import TarjimonUzState, TarjimonEnState

tarjimon = Translator()
router = Router()


@router.message(F.text == "Tarjimon bot")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer("Tarjimon bot",
                         reply_markup=language_menu())


@router.message(F.text == "🇺🇿 ➡️ 🇬🇧")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer("Matn kiriting")

    await state.set_state(TarjimonUzState.confirm)


@router.message(StateFilter(TarjimonUzState.confirm))
async def send_start(message: types.Message, state: FSMContext):
    data = tarjimon.translate(text=message.text, src="uz", dest="en")
    await message.answer(data.text)

    await state.set_state(TarjimonUzState.confirm)


# ////////////////////////////////////////////////////////////////////////////////////////////////////
@router.message(F.text == "🇬🇧 ➡️ 🇺🇿")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer("Matn kiriting")

    await state.set_state(TarjimonEnState.confirm)


@router.message(StateFilter(TarjimonEnState.confirm))
async def send_start(message: types.Message, state: FSMContext):
    data = tarjimon.translate(text=message.text, src="en", dest="uz")
    await message.answer(data.text)

    await state.set_state(TarjimonEnState.confirm)
