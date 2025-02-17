import sys

def stop_command(message, bot):
    from bot import run_admin_command
    if run_admin_command(message.chat.id, bot):
        bot.send_message(message.chat.id, "Buonanotte papo")
        bot.stop_polling()
        print("Bot terminato dall'admin " + str(message.chat.id))
