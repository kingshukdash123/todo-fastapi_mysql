from app.db.connection import create_db_connection
from fastapi.responses import JSONResponse




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
                'error': 'User not found'
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

    


def createTask_query(task, user_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'INSERT INTO tasks (id, user_id, title, description, status) VALUE (NULL, %s, %s, %s, %s)'
        curr.execute(query, (user_id,task.title, task.description, task.status))
        conn.commit()

        return JSONResponse(status_code=201, content={
            'message': 'Task added successfully'
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



def fetchTask_query(task_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'SELECT * FROM tasks WHERE id = %s'
        curr.execute(query, (task_id,))
        rows = curr.fetchall()

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