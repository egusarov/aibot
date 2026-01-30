from fastapi import FastAPI
from app.api.endpoints import router
from app.models import Base
from app.db import engine

app = FastAPI(title="AI Telegram News Bot")

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api")
