from asyncio import tasks
from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

@router.put("tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task():
    return 

@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
    return

@router.delete("tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int):
    return