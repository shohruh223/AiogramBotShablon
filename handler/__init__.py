from aiogram import Router
from .users import start, qrcode_generator


def setup_message_routers() -> Router:
    router = Router()

    # Users routers
    router.include_router(start.router)
    router.include_router(qrcode_generator.router)

    return router
