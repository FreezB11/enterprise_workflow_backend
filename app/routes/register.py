from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate
from app.repository.user_repository import get_user_by_email, create_user
from app.core.security import require_admin

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    existing = get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = create_user(db, user.email, user.password, user.role)
    return {"message": "User registered successfully", "email": new_user.email}
