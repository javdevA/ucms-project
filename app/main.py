from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from typing import List
from datetime import datetime
import os

app = FastAPI(title="UCMS - University Course Management System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple in-memory data (production-ready structure)
users_db = []
courses_db = []
enrollments_db = []

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "student"

class CourseCreate(BaseModel):
    title: str
    description: str
    instructor_id: int

@app.get("/")
def read_root():
    return {"message": "UCMS Production API Running!", "status": "healthy"}

@app.post("/api/v1/users/")
def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["id"] = len(users_db) + 1
    user_dict["created_at"] = datetime.utcnow()
    users_db.append(user_dict)
    return user_dict

@app.get("/api/v1/users/")
def list_users():
    return users_db

@app.post("/api/v1/courses/")
def create_course(course: CourseCreate):
    course_dict = course.dict()
    course_dict["id"] = len(courses_db) + 1
    courses_db.append(course_dict)
    return course_dict

@app.get("/api/v1/courses/")
def list_courses():
    return courses_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
