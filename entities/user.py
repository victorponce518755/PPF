from werkzeug.security import check_password_hash, generate_password_hash
class Usuario:
    def __init__(self, id, name, username,password,is_admin,created_at,updated_at):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.created_at = created_at
        self.updated_at = updated_at
        

    @classmethod #para no instanciar la clase  
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

class UsuarioSinPassword:
    def __init__(self, id, name, username,is_admin,created_at,updated_at):
        self.id = id
        self.name = name
        self.username = username
        self.is_admin = is_admin
        self.created_at = created_at
        self.updated_at = updated_at