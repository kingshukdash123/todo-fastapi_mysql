from app.db.connection import create_db_connection
from fastapi.responses import JSONResponse

def is_exist_user(username: str):
    conn = create_db_connection()
    curr = conn.cursor(dictionary=True)
    query = """
        SELECT * FROM users 
        WHERE username = %s
    """
    curr.execute(query, (username, ))
    rows = curr.fetchone()
    return rows



def create_user_query(user):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = """
            INSERT INTO users (id, name, username, password_hash) 
            VALUE (NULL, %s, %s, %s)
        """
        curr.execute(query, (user.name, user.username, user.password))
        conn.commit()

        new_user =  fetchUser_query(user.username)
        return JSONResponse(status_code=201, content={
            'name': new_user['name'], 
            'username': new_user['username']
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



def fetchUser_query(username):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'SELECT * FROM users WHERE username = %s'
        curr.execute(query, (username,))
        rows = curr.fetchone()

        if rows:
            return rows
        else:
            return JSONResponse(status_code=404, content={
                'error': 'user not found'
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



def get_user_by_id(user_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'SELECT * FROM users WHERE id = %s'
        curr.execute(query, (user_id,))
        rows = curr.fetchone()

        if rows:
            return rows
        else:
            return JSONResponse(status_code=404, content={
                'error': 'user not found'
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