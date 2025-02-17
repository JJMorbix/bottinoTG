def stop_command(message, bot):
    bot.send_message(message.chat.id, "Buonanotte papo")
    bot.stop_polling()
