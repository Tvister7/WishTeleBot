import asyncio
import os

from bot.crud import create_user
from db import get_session, init_db
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor

load_dotenv(".env")

API_TOKEN = os.environ["TELEBOT_TOKEN"]


async def main():

    await init_db()


bot = Bot(token=API_TOKEN)
bot["db"] = get_session
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        '''
        Привет, пользователь!
        Я бот для записи твоих желаний! 
        Если ты новенький, используй команду /registrate
        ''')


@dp.message_handler(commands=["registrate"])
async def registrate_new_user(message: types.Message):
    await create_user(message)
    await message.answer(f"Спасибо за регистрацию, {message['from']['username']}!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    executor.start_polling(dp, skip_updates=True)
