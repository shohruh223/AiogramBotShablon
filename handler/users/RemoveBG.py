import time

from aiogram import types, F, Router
from rembg import remove
from io import BytesIO
from PIL import Image

router = Router()

@router.message(F.photo)
async def remove_background_handler(message: types.Message):
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    file_path = file_info.file_path
    file = await message.bot.download_file(file_path)
    input_image = Image.open(file).convert("RGB")
    buffer = BytesIO()
    output_image = remove(input_image)
    output_image.save(buffer, format="PNG")
    buffer.seek(0)
    await message.answer_document(
        types.BufferedInputFile(buffer.getvalue(), filename=f"background_removed_{message.from_user.id}{time.time()}.png"),
        caption="Mana, sizning rasmning orqa fonisiz versiyasi!")

