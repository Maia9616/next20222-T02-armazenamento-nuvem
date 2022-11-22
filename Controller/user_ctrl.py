from Model.user import User


def create_user(name):
    user = User()
    user.name = name
    user.password = ""
    return user

