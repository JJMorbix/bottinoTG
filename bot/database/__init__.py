# bot/mongodb/__init__.py
from .db_handler import MongoDBHandler
from bot import DB_URI, DB_NAME

# Initialize the MongoDB handler with the correct URI and DB name from config
mongo_handler = MongoDBHandler(uri=DB_URI, db_name=DB_NAME)

def get_mongo_handler():
    """Provide access to the singleton MongoDB handler."""
    if not mongo_handler.client:
        mongo_handler.connect()  # Ensure connection is established when it's first used
    return mongo_handler