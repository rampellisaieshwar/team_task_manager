# Team Task Manager

Team Task Manager is a full-stack web application designed for streamlined project and task management. It features secure stateless authentication, role-based access control, and a dynamic real-time dashboard.

## 🚀 Key Features

*   **Authentication:** Stateless JWT-based authentication with secure password hashing.
*   **Role-Based Access Control (RBAC):** Strict separation of privileges between `admin` users (who can create/delete data and manage assignments) and regular `member` users.
*   **Project Workspace Grouping:** Projects act as containers, allowing tasks to be natively grouped under their respective projects for clean visual hierarchy.
*   **Task Management:** Admins can dynamically assign tasks to users. Users can update their task statuses in real-time.
*   **Real-time Dashboard:** Aggregated metrics (Total, Completed, Pending, Overdue) generated directly from the database.

## 🛠️ Technology Stack

*   **Backend:** FastAPI (Python 3)
*   **Database:** PostgreSQL (Hosted via Supabase)
*   **ORM:** SQLAlchemy
*   **Validation:** Pydantic
*   **Frontend:** Vanilla JavaScript, HTML5, and CSS3 Single Page Application (SPA), served natively by FastAPI.

## 🏃‍♂️ Quick Start

Because the frontend is served entirely by the backend API, running the project requires only a single command.

### 1. Environment Setup

Ensure you have a `.env` file in the root directory containing your Supabase PostgreSQL connection string:

```env
DATABASE_URL=postgresql://user:password@host:port/database
```

### 2. Run the Application

Activate your virtual environment and install dependencies (if not already done):

```bash
source ./venv/bin/activate
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

### 3. Access the Dashboard

Open your web browser and navigate to:
`http://127.0.0.1:8000`

## 🔐 API Architecture (RESTful)

The backend follows strict REST API design principles:
*   `POST /signup` & `POST /login` (Authentication)
*   `GET /dashboard` (Metrics Aggregation)
*   `GET /users` (Team Directory)
*   `GET /projects`, `POST /projects`, & `DELETE /projects/{id}` (Project Management)
*   `GET /tasks`, `POST /tasks`, `PATCH /tasks/{id}/status`, & `DELETE /tasks/{id}` (Task Management)
