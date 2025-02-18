def admin_only(id):
    from bot import check_admin
    if check_admin(id):
        return True, ""
    return False, "Non fare il simpatico"

def no_login():
    return