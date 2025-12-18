from app.db.connection import create_db_connection
from fastapi.responses import JSONResponse




def fetchAllTask_query(user_id):
    curr = None
    conn = None

    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'SELECT * FROM tasks WHERE user_id = %s'
        curr.execute(query, (user_id,))
        rows = curr.fetchall()

        return rows
        
    except Exception as e:
        raise e
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()

    

def createTask_query(task, user_id):
    conn = None
    curr = None

    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'INSERT INTO tasks (id, user_id, title, description, status) VALUE (NULL, %s, %s, %s, %s)'
        curr.execute(query, (user_id,task.title, task.description, task.status))
        conn.commit()

        task_id = curr.lastrowid
        curr.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        
        return curr.fetchone()

    except Exception as e:
        raise e
    
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
        return rows
        
    except Exception:
        raise
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()



def deleteTask_query(task_id):
    curr = None
    conn = None

    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = """
            DELETE FROM tasks
            WHERE id = %s
        """
        curr.execute(query, (task_id,))
        conn.commit()

        return curr.rowcount   
        
    except Exception:
        raise
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()            



def updateTask_query(task_id, task_details):
    update = []
    params = []
    curr = None
    conn = None

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
        return 0

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

        return curr.rowcount
        
    except Exception:
        raise
    
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()
    

