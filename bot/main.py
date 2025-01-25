from telegram.ext import Updater
from bot.handlers import setup_handlers
from config.settings import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Регистрация обработчиков
    setup_handlers(dp)
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()