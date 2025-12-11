import mysql.connector
from fastapi.responses import JSONResponse
from app.config.db import DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DB_NAME


myconn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER, 
        password=DB_PASSWORD, 
        port=DB_PORT, 
        database=DB_NAME
    )


def create_db_connection():
    try:
        return myconn
    except Exception as e:
        return JSONResponse(status_code=500, content={
            'Database server error : ', e
        })