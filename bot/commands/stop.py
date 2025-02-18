def stop_command(message, bot):
    bot.send_message(message.chat.id, "Buonanotte papo")
    bot.stop_polling()
    print("Bot terminato dall'admin " + str(message.chat.id))
