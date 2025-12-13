from fastapi import APIRouter, Depends
from app.db.query.tasks import fetchAllTask_query, createTask_query, fetchTask_query, deleteTask_query, updateTask_query
from app.schemas.tasks import CreateTask, UpdateTask
from app.auth.utils import get_current_user



route = APIRouter(prefix="/tasks", tags=["Tasks"])



@route.get("/")
def all_tasks(user = Depends(get_current_user)):
    all_tasks = fetchAllTask_query(user['id'])
    return all_tasks

@route.post("/create")
def create_task(task_details: CreateTask, user = Depends(get_current_user)):
    return createTask_query(task_details, user['id'])

@route.get("/{task_id}")
def fetch_task(task_id, user = Depends(get_current_user)):
    return fetchTask_query(task_id)

@route.put("/update/{task_id}")
def update_task(task_id: int, task_details: UpdateTask, user = Depends(get_current_user)):
    return updateTask_query(task_id, task_details)

@route.delete("/delete/{task_id}")
def delete_task(task_id, user = Depends(get_current_user)):
    return deleteTask_query(task_id)
