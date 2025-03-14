from aiogram import Router, types, F
from handler.users.start import check_subscription
from keyboard.inline.member_group import subscribe_ikm

router = Router()


@router.callback_query(F.data == "tekshirsh")
async def check_subscription_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    is_subscribed = await check_subscription(callback.bot, user_id)

    if is_subscribed:
        await callback.message.answer("✅ Obuna tasdiqlandi! Endi botdan foydalanishingiz mumkin.")
    else:
        await callback.message.answer(
            "❌ Siz hali obuna bo'lmagansiz. Iltimos, obuna bo'ling va qayta tekshirishni bosing.",
            reply_markup=subscribe_ikm()
        )

    await callback.answer()
