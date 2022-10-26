from models.base import Role
from helpers.db import session


if __name__ == '__main__':


    # # Get all roles from the DB
    # roles = session.query(Role).all()
    # # print('roles', roles)
    #
    # # Get filtered objects.
    # roles = session.query(Role).filter(Role.id % 2 == 0).all()
    # # print('roles', roles)
    #
    # # Get only first result
    # role = session.query(Role).first()
    # # print('role', role)
    #
    # # Order results set
    # role = session.query(Role).order_by(Role.id.desc()).first()
    # # print('role', role)
    #
    # # Insert a new role into database
    # new_role = Role(name='my_new_role')
    # print('new_role', new_role)
    # session.add(new_role)
    # session.commit()

    # roles_query = session.query(Role)
    #
    # filter_condition = random.choice([True, False])
    # print('filter_condition', filter_condition)
    #
    # if filter_condition:
    #     roles_query = roles_query.filter(Role.name == 'student')
    #
    # print('roles_query', roles_query)
    #
    # roles = roles_query.all()
    # print('roles', roles)

    new_role_1 = Role(name='new_role_1')
    session.add(new_role_1)
    # session.commit() # add only new_role_1 to the database

    new_role_2 = Role(name='new_role_2')
    session.add(new_role_2)
    # session.commit()  # add only new_role_2 to the database

    new_role_3 = Role(name='new_role_3')
    session.add(new_role_3)
    # session.commit()  # add only new_role_3 to the database

    session.commit()
