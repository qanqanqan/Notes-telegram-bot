import os
from dotenv import load_dotenv
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message


load_dotenv('.env')
dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def say_hello(msg: Message):
    await msg.answer('Hello!')


async def main():
    bot_token = os.getenv('bot_token')
    
    bot = Bot(token=bot_token)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
