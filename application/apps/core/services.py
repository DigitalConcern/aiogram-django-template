from typing import Tuple, Union

from . import models
from os import getenv
from aiogram import Bot
from .models import User


# Register your services here
def add_user(tg_id: int, username: str) -> Tuple[models.User, bool]:
    return models.User.objects.get_or_create(
        tg_id=tg_id, username=username
    )


async def mailing(text):
    bot = Bot(getenv("BOT_API_TOKEN"))
    for user in User.objects.all():
        await bot.send_message(user.tg_id, text)
