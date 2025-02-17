import telebot
import os
from bot import TOKEN, register_handlers

# Inizializzo la variabile bot col corretto token
bot = telebot.TeleBot(TOKEN)

# Registro tutti i comandi a cui il bot dovrà rispondere
register_handlers(bot)

if __name__ == "__main__":
    print("Bot in esecuzione...")
    try:
        bot.polling(none_stop=True, skip_pending=True)
    except KeyboardInterrupt:
        print("Bot fermato con successo.")
        bot.stop_polling()