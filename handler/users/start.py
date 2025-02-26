from aiogram import Router
from aiogram import types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def send_start(message: types.Message):
    await message.answer("Salom bu Shohruh Abdurahmon tomonidan yaratilgan bot shablon!\n"
                         "Mualliflik huquqi bor shu sababli foydalanishdan oldin\n"
                         "meni duo qilib ishlating, aks holda rozi emasman!")






    
