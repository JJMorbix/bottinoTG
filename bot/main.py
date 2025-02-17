import telebot
import os
from bot import TOKEN, register_handlers

# Inizializzo la variabile bot col corretto token
bot = telebot.TeleBot(TOKEN)

# Registro tutti i comandi a cui il bot dovrà rispondere
register_handlers(bot)

if __name__ == "__main__":
    print("Bot in esecuzione...")
    bot.infinity_polling()