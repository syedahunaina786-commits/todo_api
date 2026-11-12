
# Basic CRUD To-Do List API

A RESTful To-Do List API developed using Python, FastAPI, and MongoDB Atlas.

## Technologies Used

- Python
- FastAPI
- MongoDB Atlas
- PyMongo
- Pydantic
- Uvicorn

## Features

- Create a new To-Do
- Retrieve all To-Dos
- Retrieve a single To-Do
- Update an existing To-Do
- Delete a To-Do
- Input validation
- MongoDB Atlas cloud database integration
- Error handling

## Project Structure

todo-crud-api/
- app/
  - __init__.py
  - main.py
  - database.py
  - models.py
  - schemas.py
  - routes.py
- .env
- .gitignore
- requirements.txt
- README.md

## Installation

1. Clone the repository:

   git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder:

   cd todo-crud-api

3. Create a virtual environment:

   python -m venv venv

4. Activate it:

   venv\Scripts\Activate.ps1

5. Install dependencies:

   python -m pip install -r requirements.txt

6. Create a .env file and configure MongoDB Atlas:

   MONGODB_URL=your_mongodb_connection_string
   DATABASE_NAME=todo_db
   PORT=8000

7. Run the application:

   python -m uvicorn app.main:app --reload

## API Documentation

Base URL: http://127.0.0.1:8000

| Method | Endpoint | Description |
| POST | /api/todos/ | Create To-Do |
| GET | /api/todos/ | Get all To-Dos |
| GET | /api/todos/{todo_id} | Get one To-Do |
| PUT | /api/todos/{todo_id} | Update To-Do |
| DELETE | /api/todos/{todo_id} | Delete To-Do |

## Database

MongoDB Atlas is used as the cloud database.

Database Name: todo_db

Collection Name: todos

The database connection string is stored securely in the .env file.

## API Testing

Swagger UI:

http://127.0.0.1:8000/docs

## Author

Backend Intern
