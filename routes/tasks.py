from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from auth import require_role, get_current_user

router = APIRouter()

@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("admin"))
):

    new_task = models.Task(
        title=task.title,
        description=task.description,
        assigned_to=task.assigned_to,
        project_id=task.project_id,
        due_date=task.due_date
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role == "admin":
        tasks = db.query(models.Task).all()
    else:
        tasks = db.query(models.Task).filter(models.Task.assigned_to == current_user.id).all()
    return tasks


@router.patch("/tasks/{task_id}/status", response_model=schemas.TaskResponse)
def update_task_status(
    task_id: int,
    status_update: dict,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # allow admin or assigned user
    if current_user.role != "admin" and task.assigned_to != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    new_status = status_update.get("status")
    if not new_status:
        raise HTTPException(status_code=400, detail="Missing status")

    task.status = new_status
    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Admins can update anything, Members can only update their own task's status
    if current_user.role != "admin":
        if task.assigned_to != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to update this task")
        
        # Member is only allowed to update status. Reject other fields if they try to update them
        if task_update.title is not None or task_update.description is not None or task_update.assigned_to is not None or task_update.due_date is not None:
            raise HTTPException(status_code=403, detail="Members can only update task status")
        
        if task_update.status is not None:
            task.status = task_update.status
    else:
        # Admin can update everything
        if task_update.title is not None:
            task.title = task_update.title
        if task_update.description is not None:
            task.description = task_update.description
        if task_update.status is not None:
            task.status = task_update.status
        if task_update.assigned_to is not None:
            task.assigned_to = task_update.assigned_to
        if task_update.due_date is not None:
            task.due_date = task_update.due_date

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("admin"))
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    
    return {"message": "Task deleted successfully"}
