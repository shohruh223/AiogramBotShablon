from aiogram import Router
from .users import start, states_handler


def setup_message_routers() -> Router:
    router = Router()

    # Users routers
    router.include_router(start.router)
    router.include_router(states_handler.router)

    return router
