from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: int

class TaskUpdateStatus(BaseModel):
    status: str 