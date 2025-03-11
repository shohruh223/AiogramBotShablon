import requests
from aiogram import types, F, Router
from aiogram.filters import Command
import asyncio
from aiogram.types import FSInputFile

from data.config import API_KEY
from keyboard.default.main_keyboard import location_menu, contact_menu

router = Router()

currency = 'USD'  # Asosiy valyutani belgilaymiz, bu yerda USD (AQSh dollari) tanlangan

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"


# API so'rovini yuborish uchun URL ni yaratamiz:
# `{API_KEY}` - bu sizning maxsus API kalitingiz
# `{currency}` - bu manba valyuta (USD)
# `UZS` - bu maqsad valyuta (O'zbekiston so'mi)


@router.message(Command("dollar"))
async def menu_handler(message: types.Message):
    response = requests.get(url)  # API so'rovini yuboramiz va javobni `response` o'zgaruvchisiga saqlaymiz

    json_data = response.json()  # Javob ma'lumotlarini JSON formatida o'qiymiz va `json_data` ga saqlaymiz

    kurs = json_data['conversion_rate']
    await message.answer(
        f"Dollar'dan UZS'ga aylantirish uchun son kiriting!\nHozirgi 1$ narxi: {kurs} So'm\n"
        f"\nAgar boshqa narxlarni bilishni istasangiz son kiriting!")


@router.message()
async def location_handler(message: types.Message):
    response = requests.get(
        f'{url}')  # API so'rovini yuboramiz va javobni `response` o'zgaruvchisiga saqlaymiz

    json_data = response.json()  # Javob ma'lumotlarini JSON formatida o'qiymiz va `json_data` ga saqlaymiz

    kurs = json_data['conversion_rate']
    await message.answer(f"{int(kurs) * int(message.text)}")
