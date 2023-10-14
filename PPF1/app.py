from flask import Flask
from flask_mysqldb import MySQL

# Configura la instancia de MySQL
mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'laura'
    app.config['MYSQL_DB'] = 'UserDatabase'

    # Inicializa MySQL con la aplicación
    mysql.init_app(app)

    # Registrar el Blueprint del controlador de usuario
    from controllers.UserController import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')

    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
