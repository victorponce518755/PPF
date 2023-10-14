class Usuario:
    def __init__(self, idUsuario, nombre, correo, password):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo
        self.password = password

class UsuarioSinPassword:
    def __init__(self, idUsuario, nombre, correo):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo