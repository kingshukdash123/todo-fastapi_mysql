from app.db.connection import create_db_connection
from fastapi.responses import JSONResponse

def fetchAllTask_by_user_id(user_id):
    try: 
        conn = create_db_connection()
        curr = conn.cursor(dictionary=True)
        query = 'SELECT * FROM tasks WHERE user_id = %s'
        curr.execute(query, (user_id,))
        rows = curr.fetchall()
        print(rows)
        
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