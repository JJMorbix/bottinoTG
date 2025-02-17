from bot.commands import command_handlers

def register_handlers(bot):
    for command, handler in command_handlers.items():
        @bot.message_handler(commands=[command])
        def wrapper(message, bot=bot, handler=handler):
            handler(message, bot)
            #log_message(message)  # Log each message

    @bot.message_handler(func=lambda message: not message.text.startswith("/"))
    def handle_non_command_messages(message):
        bot.send_message(message.chat.id, "Parla come mangi")
        #log_message(message)