from app.core.config import MONGO_URL, DB_NAME
from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo import MongoClient

# Create async MongoDB client
client = AsyncIOMotorClient(MONGO_URL)
# client = MongoClient(MONGO_URL)

# Select database
db = client[DB_NAME]

# Select collection
log_collection = db["logs"]


def get_log_collection():
    """
    Dependency that returns the MongoDB collection.
    This allows fastAPI dependency injection if needed later
    """
    return log_collection