import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
DB_URI = os.getenv('DB_URI')
DB_NAME = os.getenv('DB_NAME')

def load_env_variables():
    if not TOKEN:
        raise ValueError("Nessun TOKEN per bot assegnato alle variabili d'ambiente")
    if not DB_URI or not DB_NAME:
        raise ValueError("Le credenziali per la connessione al db non sono assegnate alle variabili d'ambiente")

    print("Configurazione del bot caricata")