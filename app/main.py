from fastapi import FastAPI
from app.database import Base, engine
from app.models import user, task

app = FastAPI(
    title="Enterprise Workflow Management System",
    description ="Backend system for managing tasks with role-based access",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "OK"} 


