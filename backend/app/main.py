from fastapi import FastAPI
from app.routes.tasks import route as tasks_routes
from app.routes.auth import route as auth_routes

app = FastAPI(title='Todo App')

app.include_router(auth_routes)
app.include_router(tasks_routes)

@app.get("/")
def root():
    return {"status": "ok", "message": "Todo backend running"}