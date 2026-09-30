from fastapi import APIRouter, HTTPException

from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter()

# In-memory storage
tasks_db: dict[int, dict] = {}
next_id: int = 1


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=201,
    summary="Создать новую задачу",
    description=(
        "Создаёт новую задачу и возвращает её данные с присвоенным идентификатором.\n\n"
        "**Параметры тела запроса:**\n"
        "- `title` (str, обязательно): заголовок задачи, от 3 до 100 символов.\n"
        "- `description` (str | None, необязательно): описание задачи.\n"
        "- `priority` (int, обязательно): приоритет задачи, от 1 до 5.\n\n"
        "**Возможные ошибки:**\n"
        "- **422 Validation Error** — ошибка валидации: `title` короче 3 или длиннее 100 символов,\n"
        "  `priority` вне диапазона 1–5, либо пропущено обязательное поле."
    ),
)
async def create_task(task: TaskCreate):
    
    global next_id

    task_data = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
    }

    tasks_db[next_id] = task_data
    next_id += 1

    return task_data


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Получить задачу по идентификатору",
    description=(
        "Возвращает задачу с указанным идентификатором. Если задача не найдена, возвращает ошибку 404.\n\n"
        "**Параметры пути:**\n"
        "- `task_id` (int, обязательно): уникальный идентификатор задачи.\n\n"
        "**Возможные ошибки:**\n"
        "- **404 Not Found** — задача с указанным `task_id` не найдена.\n"
        "- **422 Validation Error** — `task_id` не является корректным целым числом."
    ),
)
async def get_task(task_id: int):
    
    task = tasks_db.get(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task
