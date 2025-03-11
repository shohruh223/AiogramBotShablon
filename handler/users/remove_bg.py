from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from rembg import remove
from io import BytesIO
from PIL import Image
from keyboard.default.default_keyboard import main_menu
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states.main import remove_bg


router = Router()


@router.message(F.text == "remove bg bot")
async def send_start(message: types.Message, state: FSMContext):
    await message.answer(text="Sizga nima haqida ma'lumot kerak", reply_markup=main_menu())
    await state.set_state(remove_bg.data)

@router.message(F.photo)
async def remove_background_handler(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file = await message.bot.download(photo.file_id)
    input_image = Image.open(file).convert("RGB")
    buffer = BytesIO()
    output_image = remove(input_image)
    output_image.save(buffer, format="PNG")
    buffer.seek(0)
    await message.answer_document(
        types.BufferedInputFile(buffer.getvalue(), filename="background_removed.png"),
        caption="Mana, sizning rasmning orqa fonisiz versiyasi!"
    )
    await state.set_state(remove_bg.data)

