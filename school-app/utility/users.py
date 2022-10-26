from faker import Faker
from models import User
from utility.security import get_hashed_password

fake = Faker()


def generate_fake_user(unique_identifier, role_id):
    email = fake.email()
    email = email.replace('@', f'{unique_identifier}@')

    user = User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=email,
        password=get_hashed_password('python123'),
        role_id=role_id
    )

    return user
