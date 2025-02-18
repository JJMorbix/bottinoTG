async def stop_command(update, context):
    await context.bot.send_message(chat_id=update.message.chat.id, text="Buonanotte papo")
    from bot.main import stop_bot
    print("Bot terminato dall'admin " + str(update.message.chat.id))
    await stop_bot()