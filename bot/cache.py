from typing import List
from bot.database import get_mongo_handler

class UserCache:
    _instance = None
    _registered_users: List[int] = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._registered_users:
            self.load_registered_users_from_db()

    def load_registered_users_from_db(self):
        """Load the registered users from the database into the cache."""
        db_handler = get_mongo_handler()
        query = {}  # "_id" is the default field in MongoDB for unique identifiers
        result = db_handler.find_documents("Utenti", query)
        _registered_users = [user['_id'] for user in result]

    def check_user(self, user_id: int) -> bool:
        """Check if a user is registered."""
        # First, check in the cache
        if user_id in self._registered_users:
            return True
        
        # If not in cache, query the DB
        return self.is_user_registered_in_db(user_id)

    def is_user_registered_in_db(self, user_id: int) -> bool:
        """Check the database if the user is registered."""
        db_handler = get_mongo_handler()
        
        query = {"_id": user_id}  # "_id" is the default field in MongoDB for unique identifiers
        result = db_handler.find_documents("Utenti", query)

        # Check if the user was found
        if result:
            # Add the user to the cache if they are registered
            print(f"Ho memorizzato {user_id} tra gli utenti registrati")
            self._registered_users.append(user_id)
            return True
        
        print("User not found.")
        return False

    def add_user(self, user_id: int, username: str):
        """Add a user to the cache and the database."""
        # Add the user to the cache
        self._registered_users.append(user_id)
        
        # Add the user to the database
        db_handler = get_mongo_handler()
        db_handler.insert_document("Utenti", {"_id": user_id, "username": username})