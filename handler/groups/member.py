from aiogram import types, Router, F
from aiogram.enums import ChatType
from filters.group_chat import IsGroup

router = Router()

# hurmatli mentorlar bu kod __init__ da ban faylidan oldinda bo'lishi shart, sababi ban faylida xuddi
# echo bot kabi filterlash yo'q va 1 chi shu bot ishlaydi, agar siz member faylini undan oldinga qo'ysangiz
# 1 chi member ishlaydi

@router.message(IsGroup(), F.new_chat_members)
async def new_member(message: types.Message):
    user_id = message.new_chat_members[0].id
    user_name = message.new_chat_members[0].full_name

    member = f'<a href="tg://user?id={user_id}">{user_name}</a>'
    await message.answer(f"Xush kelibsiz, {member}.",
                         parse_mode="HTML")


@router.message(IsGroup(), F.left_chat_member)
async def banned_member(message: types.Message):
    user_id = message.left_chat_member.id
    user_name = message.left_chat_member.full_name
    left_member = f'<a href="tg://user?id={user_id}">{user_name}</a>'
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{left_member} guruhni tark etdi.",
                             parse_mode="HTML")
    else:
        await message.answer(f"{left_member} guruhdan haydaldi.",
                             parse_mode="HTML")

