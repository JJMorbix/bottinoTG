import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

def load_env_variables():
    if not TOKEN:
        raise ValueError("Nessun TOKEN per bot assegnato alle variabili d'ambiente")

print("Configurazione del bot caricata")