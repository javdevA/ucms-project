from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    grade = Column(String, default="Pending")
    student = relationship("User", foreign_keys=[student_id])
    course = relationship("Course")
