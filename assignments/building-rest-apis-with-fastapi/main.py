from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


# TODO: Add GET /tasks/{task_id} and return 404 if the task does not exist.
# TODO: Add POST /tasks. Validate its body with TaskCreate and return 201.
# TODO: Add PUT /tasks/{task_id} and DELETE /tasks/{task_id}.
# TODO: Return 404 for missing tasks and 204 after a successful deletion.
