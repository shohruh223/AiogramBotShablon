from io import BytesIO
from aiogram import Bot, Dispatcher, types, F
import asyncio
from keyboard.default.default_keyboard import main_menu, back_menu

from aiogram import types, Router
import qrcode
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from states.main import QRCodeState
from aiogram.types import BufferedInputFile

router = Router()

@router.message(F.text == "QR code bot")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Link tashlang sizga qr code \n"
                              f"korinishida qilib beraman",
                         reply_markup=main_menu())
    await state.set_state(QRCodeState.data)

@router.message(StateFilter(QRCodeState.data))
async def generate_qr_code(message: types.Message, state: FSMContext):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message.text)
    qr.make(fit=True)

    image = qr.make_image(fill_color="red", back_color="white")
    buffer = BytesIO()
    image.save(buffer, "PNG")
    buffer.seek(0)
    photo = BufferedInputFile(buffer.getvalue(), filename="qrcode.png")

    await message.answer_photo(photo=photo)
    await state.set_state(QRCodeState.confirm)
