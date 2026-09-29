from fastapi import APIRouter, HTTPException

from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter()

# In-memory storage
tasks_db: dict[int, dict] = {}
next_id: int = 1


@router.post("/", response_model=TaskResponse, status_code=201)
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


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    task = tasks_db.get(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task
