from sqlalchemy.orm import Session
from app.models.task import Task

def create_task(db: Session, title: str, description: str, assigned_to: int):
    task = Task(title=title, description=description, assigned_to=assigned_to)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_user_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.assigned_to == user_id).all()

def update_task_status(db: Session, task: Task, new_status: str):
    task.status = new_status
    db.commit()
    db.refresh(task)
    return task
