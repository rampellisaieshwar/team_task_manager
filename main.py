from datetime import datetime

from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import models
from database import engine, get_db
from auth import get_current_user

from routes import users, projects, tasks

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# Serve simple static SPA
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/")
def home():
    # serve the simple SPA so visiting root shows the UI
    return FileResponse("frontend/spa.html")


# Include modular routers
app.include_router(users.router, tags=["users"])
app.include_router(projects.router, tags=["projects"])
app.include_router(tasks.router, tags=["tasks"])


# Dashboard summary
@app.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # RBAC logic: admin sees total stats, member sees only their stats
    if current_user.role == "admin":
        total = db.query(models.Task).count()
        completed = db.query(models.Task).filter(models.Task.status == "completed").count()
        pending = db.query(models.Task).filter(models.Task.status == "pending").count()
        
        now = datetime.utcnow()
        overdue = db.query(models.Task).filter(models.Task.due_date != None).filter(models.Task.due_date < now).filter(models.Task.status != "completed").count()
    else:
        total = db.query(models.Task).filter(models.Task.assigned_to == current_user.id).count()
        completed = db.query(models.Task).filter(models.Task.assigned_to == current_user.id, models.Task.status == "completed").count()
        pending = db.query(models.Task).filter(models.Task.assigned_to == current_user.id, models.Task.status == "pending").count()
        
        now = datetime.utcnow()
        overdue = db.query(models.Task).filter(
            models.Task.assigned_to == current_user.id,
            models.Task.due_date != None,
            models.Task.due_date < now,
            models.Task.status != "completed"
        ).count()

    return {
        "total_tasks": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue
    }