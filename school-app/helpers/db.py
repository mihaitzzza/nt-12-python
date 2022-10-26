from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User
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
