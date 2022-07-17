from enum import Enum

from fastapi import HTTPException

class TaskException(Enum):
    TASK_NOT_FOUND = HTTPException(status_code=404, detail="Task not found")