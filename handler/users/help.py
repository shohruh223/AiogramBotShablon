from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram import Router

router = Router()


@router.message(Command("help"))
async def send_start(message: types.Message):
    await message.answer(text="Sizda qanday muammo bor")