from aiogram import Router, types, F
from utils.youtube_service import youtube_down, extract_video_id

router = Router()


@router.message(F.text.startswith(("https://youtube.com/", "https://www.youtube.com/")))
async def download_video(message: types.Message):
    video_url = message.text
    video_id = extract_video_id(video_url)
    await message.answer("Videoni yuklash uchun ma'lumotlar olinmoqda... ⏳")

    download_link = youtube_down(video_id)
    if download_link:
        await message.answer_video(video=download_link, caption="Mana sizning videongiz! ✅")
    else:
        await message.answer("Kechirasiz, videoni yuklab bo‘lmadi. ❌")



