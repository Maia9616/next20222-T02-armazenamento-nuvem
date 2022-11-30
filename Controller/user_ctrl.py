import hashlib

from Model.models import User


def create_user(name):
    user = User()
    user.name = name
    user.email = "email"
    user.password = hashlib.sha256(user.password.encode("UTF-8")).hexdigest()
    return user

