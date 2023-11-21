from entities.user import Usuario as User
from entities.user import UsuarioSinPassword as UserSinPassword
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash


#class Usuario:
#def __init__(self, id, name, username,password,is_admin,created_at,updated_at)
class ModelUser:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_user(self, user):
        cursor = self.mysql.connection.cursor()
        password_hash = generate_password_hash(user.password)  # Genera el hash de la contraseña
        cursor.execute(
            'INSERT INTO identity (name, username, password, is_admin,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s)',
            (user.name, user.username, password_hash, user.is_admin, user.created_at, user.updated_at)
        )
        self.mysql.connection.commit()
        cursor.close()

        
    def get_userNoPassword(self,user_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT id, name,username ,is_admin, created_at,updated_at FROM identity WHERE id = %s', (user_id,))
        user_data = cursor.fetchone()
        print(user_data)
        cursor.close()

        if user_data:
            user = UserSinPassword(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
            return user
        else:
            return None

        
    def find_user_by_credentials(self, username, password):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT id, name, username, password, is_admin, created_at, updated_at FROM identity WHERE username = %s AND password = %s', (username, password))
        user_data = cursor.fetchone()
        cursor.close()

        if user_data:
            user = User(user_data[0], user_data[1], user_data[2], password, user_data[3], user_data[4], user_data[5], user_data[6])
            return user
        else:
            return None




