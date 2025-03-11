from aiogram import Router
from .users import start, dollar


def setup_message_routers() -> Router:
    router = Router()

    # Users routers
    router.include_router(start.router)
    router.include_router(dollar.router)

    return router
