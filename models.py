from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    role = Column(String)

    tasks = relationship("Task", back_populates="user")
    projects_created = relationship("Project", back_populates="creator")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    description = Column(String)
    created_by = Column(Integer, ForeignKey("users.id"))

    tasks = relationship("Task", back_populates="project")
    creator = relationship("User", back_populates="projects_created")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    description = Column(String)
    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True)

    assigned_to = Column(Integer, ForeignKey("users.id"))

    project_id = Column(Integer, ForeignKey("projects.id"))

    user = relationship("User", back_populates="tasks")

    project = relationship("Project", back_populates="tasks")

    @property
    def assignee_name(self):
        return self.user.name if self.user else None

    @property
    def project_name(self):
        return self.project.title if self.project else None