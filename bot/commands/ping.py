async def ping_command(update, context):
    message = update.message
    text_to_echo = message.text[len('/ping '):].strip() if message.text.strip().startswith('/ping') else ""
    response = f"Pong {text_to_echo}" if text_to_echo else "Pong"
    await context.bot.send_message(chat_id=message.chat.id, text=response)