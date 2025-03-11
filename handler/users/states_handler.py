from aiogram import types, Router, F
from keyboard.default.main_keyboard import back, menu
from aiogram.fsm.context import FSMContext
from states.user import UserState
from aiogram.filters import StateFilter

router = Router()


@router.message(F.text == "User")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(text=f"Ismingizni kiriting",
                         reply_markup=back())
    await state.set_state(UserState.name)


@router.message(StateFilter('*'), F.text == "Back")
async def back_from_name(message: types.Message, state: FSMContext):
    await message.answer("Asosiy menyuga qaytdingiz!", reply_markup=menu())
    await state.clear()


@router.message(StateFilter(UserState.name))
async def send_welcome(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=f"Yoshingizni kiriting",
                         reply_markup=back())
    await state.set_state(UserState.age)


@router.message(StateFilter(UserState.age))
async def send_welcome(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(text=f"Yashash manzilingizni kiriting",
                         reply_markup=back())
    await state.set_state(UserState.address)


@router.message(StateFilter(UserState.address))
async def send_welcome(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer(text="Rasmigizni kiriting",
                         reply_markup=back())
    await state.set_state(UserState.photo)


@router.message(StateFilter(UserState.photo), F.photo)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    address = data.get("address")

    photo = message.photo[-1]
    photo_file_id = photo.file_id

    await message.answer_photo(
        photo=photo_file_id,
        caption=f"{name}ning yoshi {age} da.\n"
                f"Yashash manzili: {address}")
    await state.clear()

# havasni qolgan qismini qilish
