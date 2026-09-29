from fastapi import FastAPI

from app.routers import tasks

app = FastAPI(
    title="FastAPI Project",
    description="A FastAPI application with basic structure",
    version="0.1.0",
)

app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])


@app.get("/", tags=["health"])
async def root():
    return {"message": "Welcome to FastAPI Project"}


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}
