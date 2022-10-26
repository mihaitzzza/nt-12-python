from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN
from sqlalchemy.orm import relationship
from models.base import DeclarativeBase, BaseModel
from models.users import User


class Course(DeclarativeBase, BaseModel):
    __tablename__ = 'courses'

    name = Column(VARCHAR(255), unique=True)
    is_active = Column(BOOLEAN, default=False)
    hours = Column(INTEGER, default=10)

    teacher_id = Column(INTEGER, ForeignKey(User.id))
    teacher = relationship(User)


class StudentCourse(DeclarativeBase, BaseModel):
    __tablename__ = 'student_courses'

    user_id = Column(INTEGER, ForeignKey(User.id))
    user = relationship(User)

    course_id = Column(INTEGER, ForeignKey(Course.id))
    course = relationship(Course)

    grade = Column(INTEGER, nullable=True, default=None)
