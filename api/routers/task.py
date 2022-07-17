from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.cruds.task as task_cruds
import api.schemas.user as user_schemas
import api.schemas.task as task_schemas
import api.cruds.user as user_cruds
from api.exceptions.http_exception.task_exception import TaskException

router = APIRouter()

@router.get("/tasks", response_model=List[task_schemas.Task])
async def list_tasks(db: AsyncSession = Depends(get_db), current_user: user_schemas.ResponseUser = Depends(user_cruds.get_current_active_user)):
    return await task_cruds.get_tasks_with_done(db, current_user.userid)

@router.post("/tasks", response_model=task_schemas.TaskCreateResponse)
async def create_task(task_body: task_schemas.TaskCreate, current_user: user_schemas.ResponseUser = Depends(user_cruds.get_current_active_user), db: AsyncSession = Depends(get_db)):
    return await task_cruds.create_task(db, task_body, current_user.userid)

@router.put("/tasks/{task_id}", response_model=task_schemas.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schemas.TaskCreate, db: AsyncSession = Depends(get_db), current_user: user_schemas.ResponseUser = Depends(user_cruds.get_current_active_user)):
    task = await task_cruds.get_task(db, task_id=task_id, userid=current_user.userid)
    if task is None:
        raise TaskException.TASK_NOT_FOUND
    if task.title == task_body.title:
        return task_schemas.TaskCreateResponse(title=task_body.title, id=task_id)
    
    return await task_cruds.update_task(db, task_body, original=task, userid=current_user.userid)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: user_schemas.ResponseUser = Depends(user_cruds.get_current_active_user)):
    task = await task_cruds.get_task(db, task_id=task_id, userid=current_user.userid)
    if task is None:
        raise TaskException.TASK_NOT_FOUND
        
    return await task_cruds.delete_task(db, original=task, userid=current_user.userid)