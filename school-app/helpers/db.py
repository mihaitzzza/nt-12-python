from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User, StudentCourse, Course
from utility.enums import RoleTypes
from utility.security import get_hashed_password

session = Session(
    create_engine(
        'mysql+mysqldb://root:Mihai10!@localhost:3306/nt12pythonschool'
    )
)


def authenticate(email, password):
    hashed_password = get_hashed_password(password)

    user = (
        session.query(User)
            .filter(User.email == email)
            .filter(User.password == hashed_password)
            .first()
    )

    return user


def get_student_courses(student):
    if student.role.name != RoleTypes.student:
        raise ValueError(f'{student.first_name} {student.last_name} is not a student!')

    return session.query(StudentCourse).filter(StudentCourse.user == student).all()


def get_all_courses():
    return session.query(Course).all()


def set_active_course(course_id, value=True):
    print('course_id', course_id, value)

    course = session.query(Course).filter(Course.id == course_id).first()

    course.is_active = value

    session.add(course)
    session.commit()
