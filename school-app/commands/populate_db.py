import sys
sys.path.append('../school-app')

from hashlib import sha256
from faker import Faker
from models import Role, Course, StudentCourse
from helpers.db import session
from utility.enums import RoleTypes
from utility.users import generate_fake_user


if __name__ == '__main__':
    fake = Faker()

    roles = session.query(Role.id, Role.name).all()
    roles = {
        name: id_
        for id_, name in roles
    }

    for index in range(3):
        teacher = generate_fake_user(index, roles[RoleTypes.teacher])
        session.add(teacher)

    students = []
    for index in range(100):
        student = generate_fake_user(index, roles[RoleTypes.student])
        students.append(student)
        session.add(student)

    for index in range(10):
        course = Course(
            name=fake.city()
        )
        session.add(course)

        for student in students[index * 10:index * 10 + 10]:
            student_course = StudentCourse(
                user=student,
                course=course
            )
            session.add(student_course)

    session.commit()
