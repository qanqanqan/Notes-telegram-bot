from aiogram import Router, F, html
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from .constants import COMMANDS


na_router = Router()


@na_router.message(F.text.lower() == COMMANDS["create note"])
async def answer_create_note(message: Message):
    text = "Write it's text"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


# Ew.....
# TODO next time gotta use COMMANDS constant
@na_router.message(F.text.lower() != COMMANDS["create note"])
async def answer_no(message: Message):
    text = "I don't understand you. Please, try again..."
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
