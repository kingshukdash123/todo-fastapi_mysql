from fastapi import APIRouter, Depends, Response, HTTPException
from app.schemas.auth import CreateUser, LogInUser
from app.auth.utils import signup_user, login_user, get_current_user


route = APIRouter(prefix="/auth", tags=["Auth"])

@route.post('/signup')
def signup(user: CreateUser):
    return signup_user(user)

@route.post('/login')
def login(user: LogInUser, response: Response):
    return login_user(user, response)

@route.post('/logout')
def logout(response : Response):
    try:
        response.delete_cookie(
            key="access_token",
            httponly=True,
            secure=True,
            samesite="none", 
            path="/"
        )
        return {"message": "Logged out successfully"}
    except Exception as e:
        # optional: log the error
        print(f"Logout error: {e}")
        raise HTTPException(status_code=500, detail="Logout failed")


@route.get("/me")
def about_me(user = Depends(get_current_user)):
    return {
        'id': user['id'], 
        'name': user['name'], 
        'username': user['username'], 
    }