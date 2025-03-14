from aiogram import Router, types, F
from utils.instagram_service import downloader


router = Router()
# https://www.instagram.com/

@router.message(F.text.startswith(("https://instagram.com/", "https://www.instagram.com/")))
async def instagram_down(message: types.Message):
    await message.reply("📥 Media yuklanmoqda! 2 soniya kuting...")
    data = downloader(link=message.text)

    if data == "error":
        await message.answer("❌ Bu linkda hech qanday ma'lumot yo'q")
        return

    if data["type"] == "image":
        await message.answer_photo(photo=data["media"])

    elif data["type"] == "video":
        await message.answer_video(video=data["media"])

    elif data['type'] == 'carousel':
        for i in data["media"]:
            await message.answer_document(document=i['media'])




