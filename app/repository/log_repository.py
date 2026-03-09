from bson import ObjectId
from app.db.mongodb import log_collection


async def insert_log(log):

    result = await log_collection.insert_one(log)

    return result.inserted_id


# retrieves logs from mongodb
async def get_logs(limit: int = 100, level: str | None = None):
    """
    Fetch logs from MongoDB with optional filtering and Pagination

    The repository layer is responsible for
    interacting directly with the database.
    """

    # Fetch documents from MongoDB

    query = {}

    #filter by level if provided
    if level:
        query["level"] = level

    # logs = list(log_collection.find().limit(100))

    log_cursor = log_collection.find(query).limit(limit)

    logs = []

    # Convert MongoDB ObjectId to string
    # because JSON cannot serialize ObjectId
    async for log in log_cursor:
        log["id"] = str(log["_id"])
        del log["_id"]
        logs.append(log)

    return logs



async def get_log_by_id(log_id: str):
    """
    Fetch a single log from MongoDB by its ObjectId.
    """

    log = await log_collection.find_one({"_id": ObjectId(log_id)})

    if log:
        log["id"] = str(log["_id"])
        del log["_id"]

    return log


async def update_log(log_id: str, log_data: dict):

    result = await log_collection.update_one(
        {"_id": ObjectId(log_id)},
        {"$set": log_data}
    )

    return result.modified_count


async def patch_log(log_id: str, log_data: dict):

    result = await log_collection.update_one(
        {"_id": ObjectId(log_id)},
        {"$set": log_data}
    )

    return result.modified_count

async def delete_log(log_id: str):
    """
    Delete a log from MongoDB.
    """

    result = await log_collection.delete_one(
        {"_id": ObjectId(log_id)}
    )

    return result.deleted_count