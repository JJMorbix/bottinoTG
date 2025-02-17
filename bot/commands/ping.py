def ping_command(message, bot):
    if message.text.strip().startswith('/ping'):
        text_to_echo = message.text[len('/ping '):].strip()
        if text_to_echo:
            bot.send_message(message.chat.id, "Pong " + text_to_echo)
        else:
            bot.send_message(message.chat.id, "Pong")