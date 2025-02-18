def admin_only(id):
    from bot import check_admin
    if check_admin(id):
        return True, ""
    return False, "Non fare il simpatico"

def no_login():
    return

def unregistered_only(id):
    from bot import get_user_cache
    cache = get_user_cache()
    if not cache.check_user(id):
        return True, ""
    return False, "Sei già registrato. Non è possibile tornare indietro"