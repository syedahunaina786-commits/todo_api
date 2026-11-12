import os
import motor.motor_asyncio

# Hum direct URL daal rahe hain taake .env ka koi masla na rahe
MONGODB_URL = "mongodb+srv://syedahunaina786_db_user:syeda-user-786@cluster0.qq90auc.mongodb.net/todo_db?retryWrites=true&w=majority&compressors=zlib"
DATABASE_NAME = "todo_db"

# Async client initialize karein
client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGODB_URL,
    serverSelectionTimeoutMS=5000
)

database = client[DATABASE_NAME]
todos_collection = database["todos"]

async def check_database_connection():
    try:
        await client.admin.command("ping")
        return True
    except Exception as e:
        print(f"Database connection error: {e}")
        return False
