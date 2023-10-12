from entities.user import User
from flask_mysqldb import MySQL

class ModelUser:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_user(self, user):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)',
            (user.username, user.password, user.email)
        )
        self.mysql.connection.commit()
        cursor.close()

    def get_user(self, user_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT users.id, users.username, users.email FROM users WHERE id = %s', (user_id,))
        user_data = cursor.fetchone()
        print(user_data)
        cursor.close()

        if user_data:
            user = User(user_data[0], user_data[1], user_data[2])
            return user
        else:
            return None


