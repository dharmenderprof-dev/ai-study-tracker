from fastapi import FastAPI
from typing import List
from app.schemas import TaskCreate, TaskResponse
from app.ai import generate_ai_insights

app = FastAPI(title="AI Study & To-Do Tracker API")

# Temporary in-memory database
tasks_db = []
id_counter = 1

@app.get("/")
def home():
    return {"message": "Welcome to the AI Study Tracker API!"}

@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return tasks_db

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    global id_counter
    
    # 1. Trigger our AI layer
    ai_results = generate_ai_insights(task.title, task.description)
    
    # 2. Combine user input with AI data
    new_task = {
        "id": id_counter,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        **ai_results # Merges the AI keys into this dictionary
    }
    
    tasks_db.append(new_task)
    id_counter += 1
    return new_task
