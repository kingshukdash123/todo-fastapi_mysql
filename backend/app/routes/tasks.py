from fastapi import APIRouter, Depends, HTTPException
from app.db.query.tasks import fetchAllTask_query, createTask_query, fetchTask_query, deleteTask_query, updateTask_query
from app.schemas.tasks import CreateTask, UpdateTask
from app.auth.utils import get_current_user



route = APIRouter(prefix="/tasks", tags=["Tasks"])



@route.get("/")
def all_tasks(user = Depends(get_current_user)):
    try:
        all_tasks = fetchAllTask_query(user['id'])
        if not all_tasks:
            raise HTTPException(status_code=404, detail="task not found")
        return all_tasks 
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")   



@route.post("/create", status_code=201)
def create_task(task_details: CreateTask, user = Depends(get_current_user)):
    try:
        added_task = createTask_query(task_details, user['id'])
        return {
            'message': 'task added successfully', 
            'task': {
                'id': added_task['id'], 
                'title': added_task['title'], 
                'description': added_task['description'], 
                'status': added_task['status'], 
            }
        }
    
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")



@route.get("/{task_id}")
def fetch_task(task_id, user = Depends(get_current_user)):
    try:
        task =  fetchTask_query(task_id)
        if not task:
            raise HTTPException(status_code=404, detail='task not found')
        if task['user_id'] != user['id']:
            raise HTTPException(status_code=403, detail='not allowed')
        return task

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(status_code=500, detail='internal server error')



@route.delete("/delete/{task_id}")
def delete_task(task_id, user = Depends(get_current_user)):
    try:
        task = fetchTask_query(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="task not found")

        if task["user_id"] != user["id"]:
            raise HTTPException(status_code=403, detail="not allowed")
        
        return deleteTask_query(task_id)
    
    except HTTPException:
        raise

    except Exception:
        raise HTTPException(status_code=500, detail='internal server error')



@route.put("/update/{task_id}")
def update_task(task_id: int, task_details: UpdateTask, user = Depends(get_current_user)):
    try:
        task = fetchTask_query(task_id)
        if not task:
            raise HTTPException(status_code=404, detail='task not found')
        if task['user_id'] != user['id']:
            raise HTTPException(status_code=403, detail='not allowed to edit this task')
        
        updated = updateTask_query(task_id, task_details)
        if updated == 0:
            raise HTTPException(status_code=400, detail="No fields provided to update")
        
        return {"message": "Task updated successfully"}
    
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


