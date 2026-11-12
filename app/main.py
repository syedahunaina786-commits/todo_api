import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

# Database file se check_database_connection import ho raha hai
from app.database import check_database_connection
from app.routes.todos import router as todos_router

load_dotenv()

app = FastAPI(
    title="To-Do List API",
    description="A CRUD API built with FastAPI and MongoDB Atlas",
    version="1.0.0"
)

app.include_router(todos_router)


@app.get("/")
def home():
    return {"message": "Welcome to the To-Do List API"}


# Isko async def banaya aur await lagaya taake database response ka sahi wait ho sake
@app.get("/health")
async def health_check():
    is_connected = await check_database_connection()
    if is_connected:
        return {
            "status": "healthy",
            "database": "connected"
        }
    else:
        raise HTTPException(
            status_code=500,
            detail="Database connection failed"
        )
