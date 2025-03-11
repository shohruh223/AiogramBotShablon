from aiogram import Router
from .users import start, media


def setup_message_routers() -> Router:
    router = Router()

    # Users routers
    router.include_router(start.router)
    router.include_router(media.router)

    return router
