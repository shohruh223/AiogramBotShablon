from aiogram import Router
from .users import start



def setup_message_routers() -> Router:
    router = Router()

    # Users routers
    router.include_router(start.router)


    return router
