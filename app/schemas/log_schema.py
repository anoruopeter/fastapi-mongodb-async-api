from pydantic import BaseModel
from typing import Optional

class LogSchema(BaseModel):
    """
    Schema used for creating logs (request body).
    """

    timestamp: str
    level: str
    message: str


class LogResponse(BaseModel):
    """
    Schema used for returning logs from the API.
    """

    id: str
    timestamp: str
    level: str
    message: str


class LogUpdate(BaseModel):

    timestamp: Optional[str] = None
    level: Optional[str] = None
    message: Optional[str] = None