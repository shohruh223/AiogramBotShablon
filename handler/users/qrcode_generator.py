import qrcode
from aiogram import types, F, Router
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text)
async def menu_handler_qr(message: types.Message):
    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(message.text)
    qr.make(fit=True)

    # Generate the image and save it temporarily to disk
    image = qr.make_image(fill="black", back_color="white")
    temp_file_path = "qr_code.png"
    image.save(temp_file_path)

    # Use FSInputFile to send the file
    input_file = FSInputFile(temp_file_path)
    await message.answer_photo(photo=input_file)

