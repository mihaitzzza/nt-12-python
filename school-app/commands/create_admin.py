import sys
sys.path.append('../school-app')

from getpass import getpass
from models import User, Role
from helpers.db import session
from utility.enums import RoleTypes
from utility.security import get_hashed_password, validate_email


if __name__ == '__main__':
    first_name = input('First name: ')
    last_name = input('Last name: ')

    while True:
        email = input('E-mail: ')

        if not validate_email(email):
            print('Invalid e-mail address. Please re-type.')
            continue

        db_user = session.query(User).filter(User.email == email).first()
        print('db_user', db_user)
        if db_user is not None:
            print('E-mail already taken. Please re-type.')
            continue

        break

    while True:
        password = getpass('Password: ')
        password_confirmation = getpass('Confirm password: ')

        if password_confirmation != password:
            print('Password is not confirmed. Please re-type.')
            continue

        break

    role = session.query(Role).filter(Role.name == RoleTypes.admin).first()

    admin = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=get_hashed_password(password),
        # role_id=role.id,
        role=role
    )
    session.add(admin)
    session.commit()
