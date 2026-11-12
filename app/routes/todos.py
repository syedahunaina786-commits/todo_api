from datetime import datetime, timezone
from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from pymongo.errors import PyMongoError

from app.database import todos_collection
from app.schemas import TodoCreate, TodoUpdate

router = APIRouter(prefix="/api/todos", tags=["To-Do Tasks"])


def serialize_todo(todo):
    if not todo:
        return {}
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo.get("description"),
        "status": todo["status"],
        "createdAt": todo["createdAt"].isoformat() if isinstance(todo["createdAt"], datetime) else str(todo["createdAt"])
    }


# Connection wrapper helper function
async def get_todo_or_404(todo_id: str):
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(
            status_code=404,
            detail="To-Do task not found"
        )

    # Async driver ke sath await lagana lazmi hai
    todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="To-Do task not found"
        )

    return todo


# 1. CREATE: Add a new task (Async)
@router.post("", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    try:
        data = todo.model_dump()
        data["createdAt"] = datetime.now(timezone.utc)

        # await lagana zaroori hai
        result = await todos_collection.insert_one(data)
        created_todo = await todos_collection.find_one(
            {"_id": result.inserted_id}
        )

        return serialize_todo(created_todo)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error while creating task: {str(e)}"
        )


# 2. READ ALL: Get all tasks (Async)
@router.get("")
async def get_all_todos():
    try:
        todos = []
        # motor driver mein cursor handle karne ke liye to_list use kiya jata hai
        cursor = todos_collection.find().sort("createdAt", -1)
        async for todo in cursor:
            todos.append(serialize_todo(todo))
        return todos

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error while fetching tasks: {str(e)}"
        )


# 3. READ ONE: Get one task (Async)
@router.get("/{todo_id}")
async def get_single_todo(todo_id: str):
    try:
        todo = await get_todo_or_404(todo_id)
        return serialize_todo(todo)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error while fetching task: {str(e)}"
        )


# 4. UPDATE: Replace task details (Async)
@router.put("/{todo_id}")
async def update_todo(todo_id: str, todo: TodoUpdate):
    try:
        existing_todo = await get_todo_or_404(todo_id)

        await todos_collection.update_one(
            {"_id": existing_todo["_id"]},
            {"$set": todo.model_dump()}
        )

        updated_todo = await todos_collection.find_one(
            {"_id": existing_todo["_id"]}
        )

        return serialize_todo(updated_todo)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error while updating task: {str(e)}"
        )


# 5. DELETE: Remove a task (Async)
@router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
    try:
        existing_todo = await get_todo_or_404(todo_id)

        await todos_collection.delete_one(
            {"_id": existing_todo["_id"]}
        )

        return {"message": "To-Do task deleted successfully"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error while deleting task: {str(e)}"
        )
