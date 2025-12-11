from fastapi import APIRouter
from app.db.query.tasks import fetchAllTask_by_user_id



route = APIRouter(prefix="/tasks", tags=["Tasks"])



@route.get("/users/{user_id}")
def all_tasks_by_user_id(user_id):
    all_tasks = fetchAllTask_by_user_id(user_id)
    return all_tasks

# @route.post("/{user_id}")
# def create_task(task_details):
#     return {
#         "message" : "not implemented"
#     }

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
