from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from keyboard.default.default_keyboard import main_menu, back_menu
from states.echo import UserState

router = Router()

@router.message(F.text == "echo bot")
async def ask_name(message: types.Message, state: FSMContext):
    await message.answer(
        text="""Echo bot – bu foydalanuvchidan kelgan har 
qanday xabarni o‘sha holatda qaytarib yuboradigan oddiy bot.""",
    )
    await state.set_state(UserState.salom)



@router.message()
async def ask_name(message: types.Message, state: FSMContext):
    await message.answer(
        text="""Echo bot – bu foydalanuvchidan kelgan har 
qanday xabarni o‘sha holatda qaytarib yuboradigan oddiy bot.""",
    )
    await message.answer(text="Salom keling siz bilan yaqindan tanishamiz Ism, familiyangizni kiriting?", reply_markup=main_menu())
    await state.set_state(UserState.salom)
