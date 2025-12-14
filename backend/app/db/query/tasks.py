from app.db.connection import create_db_connection
from fastapi.responses import JSONResponse, Response




def fetchAllTask_query(user_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'SELECT * FROM tasks WHERE user_id = %s'
        curr.execute(query, (user_id,))
        rows = curr.fetchall()

        if rows:
            return rows
        else:
            return JSONResponse(status_code=404, content={
                'error': 'task not found'
            })
        
    except Exception as e:
        return JSONResponse(status_code=500, content={
            'something went wrong': f'{e}'
        })
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()

    

def createTask_query(task, user_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'INSERT INTO tasks (id, user_id, title, description, status) VALUE (NULL, %s, %s, %s, %s)'
        curr.execute(query, (user_id,task.title, task.description, task.status))
        conn.commit()

        return JSONResponse(status_code=201, content={
            'message': 'task added successfully'
        })
    
    except Exception as e:
        return JSONResponse(status_code=500, content={
            'something went wrong': f'{e}'
        })
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()



def fetchTask_query(task_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'SELECT * FROM tasks WHERE id = %s'
        curr.execute(query, (task_id,))
        rows = curr.fetchone()

        if rows:
            return rows
        else:
            return JSONResponse(status_code=404, content={
                'error': 'Task not found'
            })
        
    except Exception as e:
        return JSONResponse(status_code=500, content={
            'Something went wrong': f'{e}'
        })
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()



def deleteTask_query(task_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = """
            DELETE FROM tasks
            WHERE id = %s
        """
        curr.execute(query, (task_id,))
        conn.commit()

        if curr.rowcount == 0:
            return JSONResponse(status_code=404, content={
                "message": "task not found"
            })

        return JSONResponse(status_code=200, content={
            "message": "deleted successfully"
        })    
        
    except Exception as e:
        return JSONResponse(status_code=500, content={
            'something went wrong': str(e)
        })
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()            



def updateTask_query(task_id, task_details):
    update = []
    params = []

    if task_details.title != None:
        update.append("title = %s")
        params.append(task_details.title)

    if task_details.description != None:
        update.append("description = %s")
        params.append(task_details.description)

    if task_details.status != None:
        update.append("status = %s")
        params.append(task_details.status)

    if not update:
        return JSONResponse(status_code=400, content={
            "message": "no fields provided to update"
        })

    params.append(task_id)

    try:
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = f"""
            UPDATE tasks
            SET {", ".join(update)}
            WHERE id = %s
        """
        curr.execute(query, tuple(params))
        conn.commit()

        if curr.rowcount == 0:
            return JSONResponse(
                    status_code=404,
                    content={"message": "task not found"}
            )
        
        return JSONResponse(
            status_code=200,
            content={"message": "Task updated successfully"}
        )
    
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"something went wrong": str(e)}
        )
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()
    

