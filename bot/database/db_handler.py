from pymongo.mongo_client import MongoClient
import os

class MongoDBHandler:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        """Establish a connection to the MongoDB database."""
        if not self.client:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print(f"Connected to MongoDB database: {self.db_name}")
        return self.db

    def find_documents(self, collection_name, query):
        """Find documents in the specified collection."""
        collection = self.db[collection_name]
        return list(collection.find(query))

    def insert_document(self, collection_name, document):
        """Insert a document into the specified collection."""
        collection = self.db[collection_name]
        collection.insert_one(document)

    def close_connection(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            #print("MongoDB connection closed.")
