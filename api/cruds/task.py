from fastapi import Depends
from typing import Tuple, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select 
from api.config.security_config import SecurityConfig
import api.models.task as task_model
import api.schemas.task as task_schemas
from datetime import datetime

async def create_task(
    db: AsyncSession, task_create: task_schemas.TaskCreate, userid: int
) -> task_model.Task:
    task_create_dict = task_create.dict()
    task_create_dict.update({"userid": userid})
    now = datetime.now() # In acturally, send datetime from frontend user.
    task_create_dict.update({"start_time": now})
    task_create_dict.update({"end_time"  : now})
    task = task_model.Task(**task_create_dict)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_tasks_with_done(db: AsyncSession, userid: int) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            )
            .outerjoin(task_model.Done)
            .filter(task_model.Task.userid == userid)
        )
    )

    return result.all()

async def get_task(db: AsyncSession, task_id: int, userid: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id).filter(task_model.Task.userid == userid)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None

async def update_task(db: AsyncSession, task_create: task_schemas.TaskCreate, original: task_model.Task, userid: int) -> task_model.Task:
    original.title = task_create.title
    original.userid = userid
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()