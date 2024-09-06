from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Model for a ToDo item
class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for the ToDo items
todo_list: List[TodoItem] = []

# Create a new ToDo item
@app.post("/todos", response_model=TodoItem)
def create_todo_item(todo: TodoItem):
    for item in todo_list:
        if item.id == todo.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    todo_list.append(todo)
    return todo

# Get all ToDo items
@app.get("/todos", response_model=List[TodoItem])
def get_all_todo_items():
    return todo_list

# Get a specific ToDo item by ID
@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo_item(todo_id: int):
    for item in todo_list:
        if item.id == todo_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found.")

# Update a ToDo item
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, updated_todo: TodoItem):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Item not found.")

# Delete a ToDo item
@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            todo_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found.")
