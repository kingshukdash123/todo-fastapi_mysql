from app.auth.access_token import hash_password, verify_password, create_access_token, decode_access_token
from app.db.query.auth import create_user_query, is_exist_user, fetchUser_query
from fastapi import HTTPException
from fastapi import Depends, Response, Cookie
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def signup_user(user):
    try:
        user_exist = is_exist_user(user.username)
        if user_exist:
            raise HTTPException(status_code=400, detail='username already exist')
        
        hashed_password = hash_password(user.password)
        user.password = hashed_password
        new_user = create_user_query(user)
        if not new_user:
            raise HTTPException(status_code=500, detail='internal server error')
        return {
            "name": new_user["name"],
            "username": new_user["username"]
        }
   
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def login_user(user, response: Response):
    user_exist = is_exist_user(user.username)
    if not user_exist or not verify_password(user.password, user_exist['password_hash']):
        raise HTTPException(status_code=401, detail='invalid credentials')
    
    access_token = create_access_token(data={'sub': user_exist['username']})
    response.set_cookie(
        key="access_token",
        value=access_token, 
        httponly=True,
        max_age=3600,
        secure=True,                     # True if using HTTPS (Production)
        samesite="none"
    )
    
    return {
        'message': 'login successful',
        'user': {
            'id': user_exist['id'], 
            'name': user_exist['name'], 
            'username': user_exist['username']
        }
    }



def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail='credentials missing')
    
    token = access_token
    try:
        payload = decode_access_token(token)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    if not payload:
        raise HTTPException(status_code=401, detail='invalid or expire token')
    
    user = fetchUser_query(payload['sub'])
    if not user:
        raise HTTPException(status_code=401, detail='user not found')
    
    return user