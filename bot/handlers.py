from bot.commands import command_handlers
import json
from bot.commands.conditions import common_conditions  # Import your condition functions
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

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

def register_handlers(application):
    command_conditions = load_command_conditions("bot/commands/conditions.json")
    
    def command_wrapper(handler, command):
        async def wrapper(update: Update, context: CallbackContext):
            message = update.message
            user_id = message.from_user.id
            
            # Retrieve conditions for this command (if any)
            conditions = list(command_conditions.get(command, []))
            if common_conditions.no_login in conditions:
                conditions.remove(common_conditions.no_login)
            else:
                from bot import get_user_cache
                cache = get_user_cache()
                if not cache.check_user(user_id):
                    await context.bot.send_message(chat_id=message.chat.id, text="Non sei attualmente registrato. Premi /registra per maggiori info")
                    return
            
            # Check if all conditions are satisfied
            for condition in conditions:
                is_valid, error_message = condition(user_id)
                if not is_valid:
                    await context.bot.send_message(chat_id=message.chat.id, text=error_message)
                    return
            
            await handler(update, context)
        return wrapper
    
    for command, handler in command_handlers.items():
        application.add_handler(CommandHandler(command, command_wrapper(handler, command)))
    
    async def handle_non_command_messages(update: Update, context: CallbackContext):
        await context.bot.send_message(chat_id=update.message.chat.id, text="Parla come mangi")
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_non_command_messages))