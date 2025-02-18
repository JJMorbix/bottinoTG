import telebot
import os
import sys
from bot import TOKEN, register_handlers, load_env_variables
from bot.database import get_mongo_handler

# Inizializzo la variabile bot col corretto token
bot = telebot.TeleBot(TOKEN)

# Registro tutti i comandi a cui il bot dovrà rispondere
register_handlers(bot)

try:
    load_env_variables()
except ValueError as e:
    print("Errore durante il caricamento delle variabili d'ambiente")
    print(f"Dettagli: {str(e)}")
    sys.exit()

if __name__ == "__main__":
    print("Bot in esecuzione...")
    try:
        bot.polling(none_stop=True, skip_pending=True)
    except KeyboardInterrupt:
        bot.stop_polling()

get_mongo_handler().close_connection()
print("Bot fermato con successo.")
#shutdown connection to db