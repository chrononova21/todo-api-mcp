from src.models import TaskTable
from src.schema import Task, NewTaskResponse, StatusType

async def add_new_task(task: Task) -> NewTaskResponse:
    new_task = TaskTable.create(
        title=task.title,
        description=task.description,
        status=task.status.value,
        priority=task.priority.value,
        tags=",".join(task.tags) if task.tags else None
    )
    return NewTaskResponse(
        task_id=str(new_task.task_id),
        title=new_task.title,
        priority=new_task.priority
    )


async def get_all_tasks():
    return [task.__data__ for task in TaskTable.select()]

async def get_task_by_id(task_id: str):
    task = TaskTable.get_or_none(TaskTable.task_id == task_id)
    if not task:
        return {"error": "Task not found"}
    return task.__data__

async def update_task_by_id(task_id: str):
    task = TaskTable.get_or_none(TaskTable.task_id == task_id)
    if not task:
        return {"error": "Task not found"}

    task.status = StatusType.COMPLETED.value
    task.save()

    return {
        "message": "Task updated successfully",
        "task_title": task.title,
        "task_id": str(task.task_id)
    }

async def delete_task_by_id(task_id: str):
    task = TaskTable.get_or_none(TaskTable.task_id == task_id)
    if not task:
        return {"error": "Task not found"}

    title = task.title
    task.delete_instance()

    return {
        "message": "Task deleted successfully",
        "task_title": title,
        "task_id": str(task.task_id)
    }


