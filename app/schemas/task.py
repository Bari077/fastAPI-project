from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = None
    priority: int = Field(..., ge=1, le=5)


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: int

    class Config:
        from_attributes = True
