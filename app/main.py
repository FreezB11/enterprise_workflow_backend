from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Workflow Management System",
    description ="Backend system for managing tasks with role-based access",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "OK"} 


