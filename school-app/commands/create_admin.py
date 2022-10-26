import sys
sys.path.append('../school-app')

from getpass import getpass
from models import User, Role
from helpers.db import session
from utility.enums import RoleTypes


if __name__ == '__main__':
    first_name = input('First name: ')
    last_name = input('Last name: ')
    email = input('E-mail: ')

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
        password=password,
        # role_id=role.id,
        role=role
    )
    session.add(admin)
    session.commit()

    print(f'Create admin with', first_name, last_name, email, password)
