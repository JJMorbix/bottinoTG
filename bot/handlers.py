from bot.commands import command_handlers
import json
from bot.commands.conditions import common_conditions  # Import your condition functions

def load_command_conditions(file_path):
    """
    Loads command conditions from a JSON file and returns a dictionary
    where the key is the command name, and the value is a list of condition functions.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    command_conditions = {}

    for command_name, conditions in data.items():
        condition_functions = []
        
        for condition_name in conditions:
            condition_function = getattr(common_conditions, condition_name, None)
            
            if condition_function:
                condition_functions.append(condition_function)
            else:
                print(f"Warning: Condition '{condition_name}' not found.")
        
        command_conditions[command_name] = condition_functions
    
    return command_conditions

def register_handlers(bot):
    command_conditions = load_command_conditions("bot/commands/conditions.json")

    for command, handler in command_handlers.items():
        @bot.message_handler(commands=[command])
        def wrapper(message, bot=bot, handler=handler, command=command):
            # Retrieve conditions for this command (if any)
            conditions = list(command_conditions.get(command, []))
            if common_conditions.no_login in conditions:
                conditions.remove(common_conditions.no_login)
            else:
                from bot import get_user_cache
                cache = get_user_cache()
                if not cache.check_user(message.from_user.id):  # L'utente non è registrato
                    bot.send_message(message.chat.id, "Non sei attualmente registrato. Premi /registra per maggiori info")  # Send the specific error message
                    return

            # Check if all conditions are satisfied
            for condition in conditions:
                # Dynamically call the condition function from the common_conditions module
                is_valid, error_message = condition(message.from_user.id)
                
                if not is_valid:
                    bot.send_message(message.chat.id, error_message)  # Send the specific error message
                    return  # Stop processing this command if the condition fails

            handler(message, bot)
            #log_message(message)  # Log each message

    @bot.message_handler(func=lambda message: not message.text.startswith("/"))
    def handle_non_command_messages(message):
        bot.send_message(message.chat.id, "Parla come mangi")
        #log_message(message)