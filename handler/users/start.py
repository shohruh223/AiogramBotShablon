from aiogram import Bot, Router, types
from aiogram.filters import CommandStart

from data.config import GROUP_USERNAME
from keyboard.inline.member_group import subscribe_ikm

router = Router()


async def check_subscription(bot: Bot, user_id: int) -> bool:
    """Foydalanuvchining guruhga a'zo bo'lganligini tekshiradi"""
    member = await bot.get_chat_member(chat_id=GROUP_USERNAME, user_id=user_id)
    return member.status in ["member", "administrator", "creator"]


@router.message(CommandStart())
async def bot_start(message: types.Message, bot: Bot):
    """Botni ishga tushirganda ishlaydi"""
    await message.answer(f"Salom, {message.from_user.full_name}!")
    try:
        user_id = message.from_user.id
        is_subscribed = await check_subscription(bot, user_id)
        if is_subscribed:
            await message.reply("Botdan foydalanishingiz mumkin!")
        else:
            await message.reply(
                "Botdan foydalanish uchun avval kanalimizga obuna bo'ling:",
                reply_markup=subscribe_ikm()
            )
    except Exception as e:
        print(f"Bot Kanalda admin emas! {e}")


