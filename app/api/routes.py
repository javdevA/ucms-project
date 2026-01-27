from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from ...config.settings import settings
from ...models import Base, User, Course, Enrollment
# Import services...

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class CourseCreate(BaseModel):
    title: str
    description: str

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Hash password, save user
    hashed = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Similar endpoints for /courses/, /enroll/, /grades/, /announcements/
# (Add 5-10 more: list courses, enroll, assign grades, login JWT)
