from fastapi import APIRouter, Depends
from app.schemas.auth import CreateUser, LogInUser
from app.auth.utils import signup_user, login_user, get_current_user


route = APIRouter(prefix="/auth", tags=["Auth"])

@route.post('/signup')
def signup(user: CreateUser):
    return signup_user(user)

@route.post('/login')
def login(user: LogInUser):
    return login_user(user)

@route.get("/me")
def about_me(user = Depends(get_current_user)):
    return {
        'id': user['id'], 
        'name': user['name'], 
        'username': user['username'], 
    }