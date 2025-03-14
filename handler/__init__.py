from aiogram import Router
from .users import start, help, instagram_download, youtube_download


def setup_message_routers() -> Router:
    router = Router()

    # users
    router.include_router(start.router)
    router.include_router(help.router)
    router.include_router(instagram_download.router)
    router.include_router(youtube_download.router)

    # groups

    return router
