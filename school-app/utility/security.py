import re
from hashlib import sha256


def get_hashed_password(password):
    return sha256(password.encode()).hexdigest()


def validate_email(email):
    return re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email)
