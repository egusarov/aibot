from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="AI Telegram News Bot")

app.include_router(router, prefix="/api")
