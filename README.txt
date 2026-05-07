Team Task Manager
=================

Hi there! Welcome to the Team Task Manager, a full-stack web application I built to help teams organize their projects and stay on top of their work. My goal was to create a streamlined experience with a real-time dashboard where you can easily track metrics like what's completed, pending, or overdue at a glance.

Under the hood, the backend is powered by FastAPI, and it connects to a PostgreSQL database hosted on Supabase using SQLAlchemy. The frontend is a clean Vanilla JS and HTML single-page application served directly by the backend. I made sure to prioritize security, so the app uses stateless JWT-based authentication with secure password hashing. 

It also has strict role-based access control built right in. If you log in as an 'admin', you have the privileges to create projects and dynamically assign tasks to people. On the other hand, regular 'member' users can focus solely on their assigned work and update their task statuses in real-time. Everything is organized logically, with tasks natively grouped under their respective project workspaces.

The API itself follows a RESTful architecture, handling everything from user signups and secure logins to managing dashboard metrics, users, projects, and task updates. 

If you want to spin this up locally, just make sure you have your DATABASE_URL set in a .env file. Activate your virtual environment, and run the FastAPI server using uvicorn ($ uvicorn main:app --host 127.0.0.1 --port 8000). Then, just head over to http://127.0.0.1:8000 in your browser to check it out!

Live Deployment: 
https://etharaaiteamtaskmanager.up.railway.app

Feel free to poke around, explore the code, and test the live demo!
