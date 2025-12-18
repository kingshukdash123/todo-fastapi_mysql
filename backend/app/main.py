from fastapi import FastAPI
from app.routes.tasks import route as tasks_routes
from app.routes.auth import route as auth_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Todo App')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes)
app.include_router(tasks_routes)

@app.get("/")
def root():
    return {"status": "ok", "message": "Todo backend running"}