async def registra_command(update, context):
    from . import get_string_reader
    reader = get_string_reader()
    response = reader.read("registrazione/registra")
    response = reader.parse(response, "USERNAME", update.message.from_user.username)
    await context.bot.send_message(chat_id=update.message.chat.id, text=response, parse_mode='HTML')

async def conferma_command(update, context):
    print(f"Registrazione di @{update.message.from_user.username} (ID: {update.message.from_user.id})")
    from bot import get_user_cache
    cache = get_user_cache()
    cache.add_user(update.message.from_user.id, update.message.from_user.username)
    from . import get_string_reader
    reader = get_string_reader()
    response = reader.read("registrazione/conferma")
    await context.bot.send_message(chat_id=update.message.chat.id, text=response, parse_mode='HTML')