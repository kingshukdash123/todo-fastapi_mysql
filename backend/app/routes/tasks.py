from fastapi import APIRouter
from app.db.query.tasks import fetchAllTask_query, createTask_query
from app.schemas.tasks import CreateTasks



route = APIRouter(prefix="/tasks", tags=["Tasks"])



@route.get("/users/{user_id}")
def all_tasks_by_user_id(user_id):
    all_tasks = fetchAllTask_query(user_id)
    return all_tasks

@route.post("/{user_id}")
def create_task(task_details: CreateTasks, user_id):
    return createTask_query(task_details, user_id)

# @route.get("/{task_id}")
# def fetch_task():
#     return {
#         "message" : "not implemented"
#     }

# @route.put("/{task_id}")
# def update_task(task_details):
#     return {
#         "message" : "not implemented"
#     }

# @route.delete("/{task_id}")
# def delete_task():
#     return {
#         "message" : "not implemented"
#     }
