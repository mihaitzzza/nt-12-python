import MySQLdb


class User:
    def __init__(self, id_, first_name, last_name, email, password, role_id):
        self.id = id_
        self.first_name = first_name


if __name__ == '__main__':
    # Step 1. Get DB connection
    db_connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        database='nt12pythonschool',
        user='root',
        password='Mihai10!',
    )

    # Step 2. Get a cursor instance.
    db_cursor = db_connection.cursor()

    # Step 3. Execute SQL code.
    db_cursor.execute("SELECT * FROM users;")

    # Step 4. Print users
    users = [
        User(*db_row)
        for db_row in db_cursor.fetchall()
    ]
    print('users', users)
