from aiogram import Router, F, types

router = Router()

image = "https://robocontest.uz/storage/uploads/profile/22107aGFtonSfMNqJptFxe1z8jAJt.jpg"


@router.message(F.photo)
async def photo_handler(message: types.Message):
    await message.reply("Siz rasm yubordingiz")


@router.message(F.video)
async def video_handler(message: types.Message):
    await message.reply("Siz video yubordingiz")


@router.message(F.document)
async def document_handler(message: types.Message):
    await message.reply("Siz document yubordingiz")


@router.message(F.location)
async def location_handler(message: types.Message):
    await message.reply("Siz lokatsiya yubordingiz")


@router.message(F.contact)
async def contact_handler(message: types.Message):
    await message.reply("Siz Kontakt yubordingiz")


@router.message(F.text == "photo")
async def send_photo_handler(message: types.Message):
    await message.answer_photo(photo=image)


@router.message(F.forward_date)
async def forward_message_handler(message: types.Message):
    await message.reply("Boshqa foydalanuvchini xabarini yubordingiz")


@router.message(F.text.contains("ahmoq"))
async def handle_insult(message: types.Message):
    await message.reply("Iltimos, odobli bo‘ling!")


bad_words = ["ahmoq", "jinni", "odobsiz"]


@router.message(F.text.func(lambda text: any(word in text.lower() for word in bad_words)))
async def handle_insults(message: types.Message):
    await message.reply("Iltimos, odobli bo'ling!")


@router.message(F.text.regexp(r"^\d+$"))
async def only_numbers_handler(message: types.Message):
    await message.answer("+9989123123")


@router.message(F.text.regexp(r"^\+?\d+$"))
async def handle_numbers(message: types.Message):
    await message.reply("Siz faqat raqam yubordingiz!")


@router.message(F.text.regexp(r"^\+9989\d{8}$"))
async def handle_uzbek_numbers(message: types.Message):
    await message.reply("Siz faqat raqam yubordingiz!")


@router.message(F.text)
async def photo_handler(message: types.Message):
    await message.reply("Siz matn yubordingiz")
