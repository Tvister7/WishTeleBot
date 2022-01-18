from aiogram import types

from bot.db import get_session
from bot.models import User


async def create_user(message: types.Message):
    username = message["from"]["username"]
    user_telegram_id = message["from"]["id"]
    session = await get_session().asend(None)
    # session.begin()
    # session.add(new_user)
    # await session.commit()
    async with session.begin():
        # new_user = User(telegram_id=user_telegram_id, name=username)
        # session.add(new_user)
        await session.execute("INSERT INTO user (telegram_id, name) VALUES (?, ?)", (user_telegram_id, username, ))

