#!/bin/bash

if [ ! -f .env ]; then
    echo "Errore: il file .env (essenziale) non è stato trovato!"
    exit 1
fi

echo "Avvio del bot Telegram..."
python3 -m bot.main