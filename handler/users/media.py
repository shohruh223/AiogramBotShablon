from aiogram import types, F, Router
from aiogram.filters import Command
import asyncio
from aiogram.types import FSInputFile
from keyboard.default.main_keyboard import location_menu, contact_menu

router = Router()
image = "https://robocontest.uz/storage/uploads/profile/22107aGFtonSfMNqJptFxe1z8jAJt.jpg"
images = [
    "https://robocontest.uz/storage/uploads/profile/22107aGFtonSfMNqJptFxe1z8jAJt.jpg",
    "https://media.licdn.com/dms/image/v2/C4D03AQEI43jKPEHGww/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1661104445662?e=2147483647&v=beta&t=UtIdTs0po69CuUVecxePSpBZY0wJzNm7szXPuzBbf0s",
    "https://i.ytimg.com/vi/9XvQ-97-cxA/oar2.jpg?sqp=-oaymwEYCJUDENAFSFqQAgHyq4qpAwcIARUAAIhC&rs=AOn4CLCcyDsRcnM7TgcsKbGYyDvkIerLPg",
]


@router.message(Command("start"))
async def menu_handler(message: types.Message):
    await message.answer("Salom botga xush kelibsiz")


@router.message(Command("photo"))
async def menu_handler(message: types.Message):
    photo = FSInputFile("cat.jpg")
    await message.answer_photo(photo=photo,
                               caption="Mushukcha")


@router.message(Command("video"))
async def send_video(message: types.Message):
    video = FSInputFile("video.mp4")
    await message.answer_video(video=video, caption="Bu video")


@router.message(Command("document"))
async def send_video(message: types.Message):
    document = FSInputFile("ID kart.pdf")
    await message.answer_document(document=document, caption="Bu document")


@router.message(Command("audio"))
async def send_video(message: types.Message):
    audio = FSInputFile("sevara nazarxon-ulugimsan vatanim.mp3")
    await message.answer_audio(audio=audio,
                               caption="Sevara Nazarxon - ulug'imsan vatanim")


@router.message(Command("voice"))
async def send_video(message: types.Message):
    audio = FSInputFile("voice.ogg")
    await message.answer_voice(voice=audio, caption="Bu ovoz")


@router.message(Command("contact"))
async def send_video(message: types.Message):
    await message.answer_contact(phone_number="+998914530909",
                                 first_name="Shohruh",
                                 last_name="Abdurahmon", )


@router.message(Command("location"))
async def send_video(message: types.Message):
    latitude = 41.32397742914421
    longitude = 69.24190012531447
    await message.answer_location(latitude=latitude,
                                  longitude=longitude)


@router.message(Command("my_contact"))
async def send_video(message: types.Message):
    await message.answer(text="Telefon raqamingizni yuboring",
                         reply_markup=contact_menu())


@router.message(Command("my_location"))
async def send_video(message: types.Message):
    await message.answer(text="Joylashgan manzilingizni yuboring",
                         reply_markup=location_menu())
