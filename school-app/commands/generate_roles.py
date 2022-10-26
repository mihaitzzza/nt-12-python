import sys

# sys.path.append('/home/mihaitzzza/work/siit/nt-12-python/school-app')
sys.path.append('../school-app')

from helpers.db import session
from models import Role
from utility.enums import RoleTypes


if __name__ == '__main__':
    for role_type in RoleTypes:
        session.add(
            Role(name=role_type)
        )
    session.commit()
