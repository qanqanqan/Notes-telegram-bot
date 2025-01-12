from aiogram import Router, html
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.for_note_action import get_note_actions
from .note_action import na_router


main_router = Router()
main_router.include_router(na_router)


@main_router.message(Command("start"))
async def start_dialog(message: Message):
    text = f"Hi! It's {html.bold('Note Bot!')}\n"\
"Here you can create notes for yourself to remember stuff\n"\
"Let's start!"
    await message.answer(text, reply_markup=get_note_actions())