from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Модель для создания новой задачи."""

    title: str = Field(..., min_length=3, max_length=100, description="Заголовок задачи")
    description: str | None = Field(None, description="Описание задачи")
    priority: int = Field(..., ge=1, le=5, description="Приоритет задачи (от 1 до 5)")


class TaskResponse(BaseModel):
    """Модель для ответа с данными задачи."""

    id: int = Field(..., description="Уникальный идентификатор задачи")
    title: str = Field(..., description="Заголовок задачи")
    description: str | None = Field(None, description="Описание задачи")
    priority: int = Field(..., description="Приоритет задачи (от 1 до 5)")

    class Config:
        from_attributes = True
