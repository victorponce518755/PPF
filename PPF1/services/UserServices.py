from models.ModelUser import ModelUser
from entities.user import User

class UserService:
    def __init__(self, mysql):
        self.model_user = ModelUser(mysql)

    def create_user(self, username, password, email):
        user = User(username, password, email)
        self.model_user.create_user(user)

    def get_user(self, id):
        user = self.model_user.get_user(id)
        return user