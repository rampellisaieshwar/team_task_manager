Team Task Manager
=================

Team Task Manager is a full-stack web application designed for streamlined project and task management. It features secure stateless authentication, role-based access control, and a dynamic real-time dashboard.

Key Features:
- Authentication: Stateless JWT-based authentication with secure password hashing.
- Role-Based Access Control (RBAC): Strict separation of privileges between 'admin' users and regular 'member' users.
- Project Workspace Grouping: Tasks are natively grouped under their respective projects.
- Task Management: Admins can dynamically assign tasks. Users can update their task statuses in real-time.
- Real-time Dashboard: Aggregated metrics (Total, Completed, Pending, Overdue).

Technology Stack:
- Backend: FastAPI
- Database: PostgreSQL (Supabase)
- ORM: SQLAlchemy
- Validation: Pydantic
- Frontend: Vanilla JS/HTML SPA (served natively by FastAPI)

Quick Start:

1. Ensure you have a .env file with your DATABASE_URL.
2. Activate your virtual environment:
   $ source ./venv/bin/activate
3. Start the FastAPI server:
   $ uvicorn main:app --host 127.0.0.1 --port 8000
4. Access the web interface at:
   http://127.0.0.1:8000

API Architecture (RESTful):
- POST /signup & POST /login
- GET /dashboard 
- GET /users 
- GET /projects & POST /projects 
- GET /tasks, POST /tasks, & PATCH /tasks/{id}/status 
