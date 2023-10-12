from entities.user import User
from flask_mysqldb import MySQL

class ModelUser:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_user(self, user):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO users VALUES (NULL, %s, %s, %s)',
            (user.username, user.password, user.email)
        )
        self.mysql.connection.commit()
        cursor.close() 
    
    def get_user(self, id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
        user = cursor.fetchone()
        cursor.close()
        return user


