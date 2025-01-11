from aiogram import Router, F, html
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.for_note_action import get_note_action


COMMANDS = [
    Command('start').__str__(),
    'create note',
]

router = Router()


@router.message(Command("start"))
async def start_dialog(message: Message):
    text = f"Hi! It's {html.bold('Note Bot!')}\n"\
"Here you can create notes for yourself to remember stuff\n"\
"Let's start!"
    await message.answer(text, reply_markup=get_note_action())


@router.message(F.text.lower() == "create note")
async def answer_create_note(message: Message):
    text = "Now choose it's title"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


# Ew.....
# TODO next time gotta use COMMANDS constant
@router.message(F.text.lower() != "create note")
async def answer_no(message: Message):
    text = "I don't understand you. Please, try again..."
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
