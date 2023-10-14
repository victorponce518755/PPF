from entities.user import Usuario as User
from entities.user import UsuarioSinPassword as UserSinPassword
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

class ModelUser:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_user(self, user):
        cursor = self.mysql.connection.cursor()
        password_hash = generate_password_hash(user.password)  # Genera el hash de la contraseña
        cursor.execute(
            'INSERT INTO Usuario (nombre, correo, password) VALUES (%s, %s, %s)',
            (user.nombre, user.correo, password_hash)  # Almacena el hash de la contraseña
        )
        self.mysql.connection.commit()
        cursor.close()

    def get_user(self, user_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT idUsuario, nombre, correo FROM Usuario WHERE idUsuario = %s', (user_id,))
        user_data = cursor.fetchone()
        print(user_data)
        cursor.close()

        if user_data:
            user = User(user_data[0], user_data[1], user_data[2])
            return user
        else:
            return None
        
    def get_userNoPassword(self,user_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT idUsuario, nombre, correo FROM Usuario WHERE idUsuario = %s', (user_id,))
        user_data = cursor.fetchone()
        print(user_data)
        cursor.close()

        if user_data:
            user = UserSinPassword(user_data[0], user_data[1], user_data[2])
            return user
        else:
            return None

        
    def find_user_by_credentials(self, correo, password):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT idUsuario, nombre, correo FROM Usuario WHERE correo = %s AND password = %s', (correo, password))
        user_data = cursor.fetchone()
        cursor.close()

        if user_data:
            user = User(user_data[0], user_data[1], user_data[2])
            return user
        else:
            return None



