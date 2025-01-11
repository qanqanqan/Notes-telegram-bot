import logging
import sys
import os
from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import note_action


async def main():
    load_dotenv()
    bot_token = os.getenv('bot_token')

    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(note_action.router)
    # dp.include_router(***additional router***)

    # skip all incoming messages
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
