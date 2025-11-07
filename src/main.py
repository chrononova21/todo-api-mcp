from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from src.models import db_init
from src.schema import Task
from src.service import (
    add_new_task, get_all_tasks,
    get_task_by_id, delete_task_by_id,
    update_task_by_id
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_init()
    yield

app = FastAPI(debug=True, lifespan=lifespan)

@app.post("/task/add-task", operation_id="add_new_task")
async def add_task(task:Task):
    """
    Use this API to add a new task to the to-do list
    required params => title, description, status (in_progress, completed), priority (low, medium, high), tags
    :return: task_id, title and priority
    """
    response = await add_new_task(task=task)
    return response

@app.get("/task/all-tasks", operation_id="get_all_tasks")
async def all_tasks():
    """
    Use this API to get all the tasks
    :return: list of tasks
    """
    response = await get_all_tasks()
    return response

@app.get("/task/{task_id}", operation_id="get_task_by_id")
async def get_task_by_id_api(task_id: str):
    """
    Use this API to retrieve a particular task by task_id
    :param task_id:
    :return: object of that task with its details
    """
    response = await get_task_by_id(task_id=task_id)
    return response

@app.patch("/task/{task_id}", operation_id="update_task_by_id")
async def update_task_by_id_api(task_id: str):
    """
    Use this API to update an existing task
    :param task_id:
    :return: message, title, task_id
    """
    response = await update_task_by_id(task_id=task_id)
    return response

@app.delete("/task/{task_id}", operation_id="delete_task_by_id")
async def delete_task_by_id_api(task_id: str):
    """
    Use this API to delete an existing task
    :param task_id:
    :return: message, title, task_id
    """
    response = await delete_task_by_id(task_id=task_id)
    return response

mcp_app = FastApiMCP(app)
mcp_app.mount_http()