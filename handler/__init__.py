from aiogram import Router
from .users import start, reply_keyboard_handler, inline_keyboard_handler


def setup_message_routers() -> Router:
    router = Router()

    # Users routers
    router.include_router(start.router)
    router.include_router(reply_keyboard_handler.router)
    router.include_router(inline_keyboard_handler.router)

    return router
