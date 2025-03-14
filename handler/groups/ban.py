from aiogram import types, Router, F
from filters.group_chat import IsGroup
import asyncio

router = Router()
BAD_WORDS = ["ahmoq", "jinni", "odobsiz"]


# @router.message(IsGroup())
# async def send_welcome(message: types.Message):
#     if message.text and any(word in message.text.lower() for word in BAD_WORDS):
#         await message.reply(text="Iltimos, odobli bo'ling!")


@router.message(IsGroup())
async def send_welcome(message: types.Message):
    if message.text and any(word in message.text.lower() for word in BAD_WORDS):
        bot_message = await message.reply(text="Iltimos, odobli bo'ling!")
        await message.delete()
        await asyncio.sleep(5)
        await bot_message.delete()





