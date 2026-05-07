from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ---------- USER ----------

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True


# ---------- PROJECT ----------

class ProjectCreate(BaseModel):
    title: str
    description: str


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    created_by: Optional[int] = None

    class Config:
        orm_mode = True


# ---------- TASK ----------

class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_to: int
    project_id: int
    due_date: Optional[datetime] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[int] = None
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    assigned_to: int
    assignee_name: Optional[str] = None
    project_id: int
    project_name: Optional[str] = None
    due_date: Optional[datetime]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True