# app/main.py
from fastapi import FastAPI
from app.api.endpoints import router
from app.db.init_db import init_db

app = FastAPI(title="AI Telegram News Bot")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router, prefix="/api")
