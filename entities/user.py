from werkzeug.security import check_password_hash, generate_password_hash
class Usuario:
    def __init__(self, idUsuario, nombre, correo, password):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo
        self.password = password

    @classmethod #para no instanciar la clase  
    def check_password(self, hashed_password, contraseña):
        return check_password_hash(hashed_password, contraseña)

class UsuarioSinPassword:
    def __init__(self, idUsuario, nombre, correo):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo