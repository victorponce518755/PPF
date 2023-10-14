from models.ModelUser import ModelUser
from entities.user import Usuario as User

class UserServices:
    def __init__(self, mysql):
        self.model_user = ModelUser(mysql)

    def create_user(self, user_data):
        user = User(None, user_data['username'], user_data['password'], user_data['email'])
        self.model_user.create_user(user)

    def get_user_profile(self, user_id):
        return self.model_user.get_user(user_id)
    
    def login_user(self, correo, password):
        return self.model_user.find_user_by_credentials(correo, password)
