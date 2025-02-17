#TEMP
TEMP_ADMIN = [6652941335]

def check_admin(id):
    return id in TEMP_ADMIN

def run_admin_command(id, bot):
    if check_admin(id):
        return True
    
    bot.send_message(id, "Non fare il simpaticone")
    return False