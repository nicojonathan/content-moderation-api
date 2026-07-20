from fastapi import FastAPI
from app.routes.moderation import router

app = FastAPI(
    title="Moderation API",
    version="1.0.0"
)

app.include_router(router)