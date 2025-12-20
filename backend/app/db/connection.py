import mysql.connector
from fastapi import HTTPException
from app.config.db import DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DB_NAME



def create_db_connection():
    try:
        myconn = mysql.connector.connect(
                    host=DB_HOST,
                    user=DB_USER, 
                    password=DB_PASSWORD, 
                    port=DB_PORT, 
                    database=DB_NAME
                )
        return myconn
    
    except mysql.connector.Error as e:
        raise HTTPException(
            status_code=500, 
            detail='Database connection failed. try again...'
        )
