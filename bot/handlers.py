from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from bot.database import get_connection
from bot.keyboards import main_menu

def start(update: Update, context: CallbackContext):
    """Обработчик команды /start"""
    update.message.reply_text(
        "🏗 Construction Report Bot\nВыберите действие:",
        reply_markup=main_menu()
    )

def setup_handlers(dispatcher):
    """Регистрация всех обработчиков"""
    dispatcher.add_handler(CommandHandler("start", start))
    # Добавить другие обработчики