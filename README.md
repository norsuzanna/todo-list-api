# To-Do List API

## Overview

The **To-Do List API** is a simple and efficient backend service built using **FastAPI**. It provides a set of RESTful API endpoints for managing a list of tasks, allowing users to create, retrieve, update, and delete to-do items. This project is designed to be scalable and can be easily integrated into any task management system.

## Features

- **Create Tasks**: Add a new task with a title, description, and status (completed or not).
- **Retrieve Tasks**:
  - Get all tasks in the system.
  - Retrieve a specific task by its unique ID.
- **Update Tasks**: Modify an existing task’s title, description, or status.
- **Delete Tasks**: Remove a task by its unique ID.
- **In-Memory Storage**: Stores tasks temporarily in memory (can be extended to use a database).

## Technology Stack

- **FastAPI**: High-performance Python web framework for building APIs.
- **Uvicorn**: Lightning-fast ASGI server for serving the FastAPI app.
- **Pydantic**: Used for data validation and settings management with Python type hints.

## API Endpoints

### Create a Task

- **POST** `/todos`
  - Adds a new to-do task.
  - **Request Body**:
    ```json
    {
      "id": 1,
      "title": "Finish Project",
      "description": "Complete the project backend by tonight.",
      "completed": false
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "Finish Project",
      "description": "Complete the project backend by tonight.",
      "completed": false
    }
    ```

### Retrieve All Tasks

- **GET** `/todos`
  - Fetches all tasks.
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "title": "Finish Project",
        "description": "Complete the project backend by tonight.",
        "completed": false
      }
    ]
    ```

### Retrieve a Task by ID

- **GET** `/todos/{todo_id}`
  - Fetches a specific task by its ID.
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "Finish Project",
      "description": "Complete the project backend by tonight.",
      "completed": false
    }
    ```

### Update a Task

- **PUT** `/todos/{todo_id}`
  - Updates an existing task.
  - **Request Body**:
    ```json
    {
      "id": 1,
      "title": "Updated Project Title",
      "description": "Updated task description.",
      "completed": true
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "Updated Project Title",
      "description": "Updated task description.",
      "completed": true
    }
    ```

### Delete a Task

- **DELETE** `/todos/{todo_id}`
  - Deletes a task by its ID.
  - **Response**:
    ```json
    {
      "message": "Item deleted successfully"
    }
    ```

## How to Run the Project

1. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Run the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## Documentation

URL: https://m8vqll-8000.csb.app/docs (need to run the project first)
