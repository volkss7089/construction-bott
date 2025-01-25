from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton('/report'), KeyboardButton('/shift_start')],
        [KeyboardButton('/my_reports'), KeyboardButton('/help')]
    ], resize_keyboard=True)

def admin_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton('/all_reports'), KeyboardButton('/stats')],
        [KeyboardButton('/export_data')]
    ], resize_keyboard=True)