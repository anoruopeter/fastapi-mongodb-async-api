from app.repository.log_repository import (
    insert_log,
    get_logs,
    get_log_by_id,
    delete_log,
    update_log,
    patch_log
)


async def save_log(log):

    inserted_id = await insert_log(log)

    return str(inserted_id)

async def fetch_logs(limit: int = 100, level: str | None = None):
    """
    Service layer for retrieving logs.

    This layer contains business logic.
    It communicates between the API layer
    and the repository (database) layer.
    """

    return await get_logs(limit=limit, level=level)


async def fetch_log_by_id(log_id: str):
    """
    Service layer wrapper.
    """

    return await get_log_by_id(log_id)


async def replace_log(log_id: str, log_data: dict):

    updated =  await update_log(log_id, log_data)

    return updated


async def patch_log_service(log_id: str, log_data: dict):

    updated = await patch_log(log_id, log_data)

    return updated


async def remove_log(log_id: str):
    """
    Service wrapper for deleting logs.
    """
    return await delete_log(log_id) 