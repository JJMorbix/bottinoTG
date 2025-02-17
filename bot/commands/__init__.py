import os
import importlib

# Dizionario
command_handlers = {}

# Importo tutti i moduli di commands/
commands_folder = os.path.dirname(__file__)
for filename in os.listdir(commands_folder):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"bot.commands.{filename[:-3]}"  # Remove `.py` extension
        module = importlib.import_module(module_name)

        # Estraggo le funzioni che finiscono per `_command` (ex start_command, help_command)
        for attr in dir(module):
            if attr.endswith("_command"):
                command_name = attr[:-8]  # Rimuovo  il suffisso `_command`
                command_handlers[command_name] = getattr(module, attr)
