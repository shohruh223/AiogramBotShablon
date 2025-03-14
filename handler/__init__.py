from aiogram import Router
from .users import start, help, user
from .groups import ban, member

def setup_message_routers() -> Router:

    router = Router()

    # users
    router.include_router(start.router)
    router.include_router(help.router)
    router.include_router(user.router)

    # groups
    router.include_router(member.router)
    router.include_router(ban.router)

    return router