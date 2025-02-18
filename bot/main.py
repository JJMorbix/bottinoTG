import logging
import os
import sys
import signal
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from bot import TOKEN, register_handlers, load_env_variables
from bot.database import get_mongo_handler, close_mongo_connection

# Configure base logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Keep INFO, WARNING, ERROR
)


application = None
def get_application():
    global application
    if application is None:
        application = Application.builder().token(TOKEN).build()
    return application

async def stop_bot():
    print("Interruzione manuale del bot")
    if close_mongo_connection():
        print("Connessione al database chiusa. Bot fermato con successo.")
    application = get_application()
    try:
        await application.shutdown()
    except Exception:
        pass
    os._exit(0)

def main():
    try:
        load_env_variables()
    except ValueError as e:
        print("Errore durante il caricamento delle variabili d'ambiente")
        print(f"Dettagli: {str(e)}")
        sys.exit()
    
    # Creazione dell'applicazione bot
    application = get_application()
    
    # Registra tutti i comandi
    register_handlers(application)
    
    # Registrazione del segnale di interruzione
    signal.signal(signal.SIGINT, lambda s, f: stop_bot())  # Ctrl+C to stop the bot
    signal.signal(signal.SIGTERM, lambda s, f: stop_bot())  # Terminate signal to stop the bot

    print("Bot in esecuzione...")
    
    # Avvio del bot con il polling
    application.run_polling()  # This will keep running until stopped manually

if __name__ == "__main__":
    main()
