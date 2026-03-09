from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.schemas.log_schema import LogSchema, LogResponse, LogUpdate
from bson import ObjectId
from bson.errors import InvalidId
from app.services.log_service import fetch_logs, fetch_log_by_id, save_log, replace_log, patch_log_service, remove_log

# APIRouter allows us to organize endpoints into modules

router = APIRouter()

@router.get("/logs", response_model=List[LogResponse])
async def get_logs(limit: int = Query(100, le=100), level: Optional[str] = None):

    """
    GET /logs endpoint

    Returns logs stored in MongoDB with optional filtering and Pagination.
    """
    logs = await fetch_logs(limit=limit, level=level)
    
    return logs


@router.get("/logs/{log_id}", response_model=LogResponse)
async def get_log(log_id: str):
    """
    Fetch a single log by ID.

    Validates the MongoDB ObjectId and returns
    proper API errors if invalid or not found.
    """

    # Validate ObjectId format
    try:
        ObjectId(log_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="invalid log ID")

    log = await fetch_log_by_id(log_id)

    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    
    return log


@router.post("/logs", response_model=dict)
async def create_log(log: LogSchema):
    """
    Create a new log entry.

    FastAPI automatically validates the request
    using the LogSchema model.
    """
    log_dict = log.model_dump()

    inserted_id = await save_log(log_dict)

    return {
        "message": "Log created",
        "id": inserted_id
    }


@router.put("/logs/{log_id}")
async def update_log(log_id: str, log: LogSchema):

    log_dict = log.model_dump()

    updated = await replace_log(log_id, log_dict)

    if not updated:
        raise HTTPException(status_code=404, detail="Log not found")
    
    return {"message": "log updated"}


@router.patch("/logs/{log_id}")
async def patch_log(log_id: str, log: LogUpdate):

    log_dict = log.model_dump(exclude_unset=True)

    updated = await patch_log_service(log_id, log_dict)

    if not updated:
        raise HTTPException(status_code=404, detail="Log not found")
    
    return {"message": "log patched"}



@router.delete("/logs/{log_id}", status_code=204)
async def delete_log_route(log_id: str):
    """
    Delete a log by ID.
    """
    deleted = await remove_log(log_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Log not found")

    return