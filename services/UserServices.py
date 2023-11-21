from models.ModelUser import ModelUser
from entities.user import Usuario as User
from werkzeug.security import check_password_hash, generate_password_hash


class UserServices:
    def __init__(self, mysql):
        self.model_user = ModelUser(mysql)

    def create_user(self, user_data):
        user = User(None, user_data['username'],
                    user_data['password'], user_data['email'])
        self.model_user.create_user(user)

    def get_user_profile(self, user_id):
        return self.model_user.get_userNoPassword(user_id)

    def login_user(self, username, password):
        user = self.model_user.find_user_by_credentials(username, password)
        if user and check_password_hash(user.password, password):
            return user
        else:
            return None
        
    # lofin user, pero sin contraseña hash
    def login_user2(self, username, password):
        user = self.model_user.find_user_by_credentials(username, password)
        if user:
            return user
        else:
            return None
