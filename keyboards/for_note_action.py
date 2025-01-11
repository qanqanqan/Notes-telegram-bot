from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_note_action():
    button = KeyboardButton(text='Create note')
    keyboard = ReplyKeyboardMarkup(keyboard=[[
        button
    ]], resize_keyboard=True)
    return keyboard
