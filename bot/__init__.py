from .config import TOKEN, load_env_variables, DB_URI, DB_NAME
from .handlers import register_handlers
from .utils import *
from .cache import UserCache

user_cache = None
def get_user_cache():
    global user_cache
    if user_cache is None:
        user_cache = UserCache()    
    return user_cache

#__all__ = ["TOKEN", "DB_USER", "DB_PASS", "register_handlers", "check_admin"]