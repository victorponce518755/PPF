from flask import Flask
from flask_mysqldb import MySQL
from flask_session import Session  
from flask_cors import CORS
import os


mysql = MySQL()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuración de la base de datos
    app.config['MYSQL_HOST'] = 'database-main.cbsqc5jwwjad.us-east-2.rds.amazonaws.com'
    app.config['MYSQL_USER'] = 'admin'
    app.config['MYSQL_PASSWORD'] = 'Rtxmlp4335'
    app.config['MYSQL_DB'] = 'Conciertos3'

    # Configuración de Flask-Session
    app.config['SESSION_TYPE'] = 'filesystem'  # Almacena las sesiones en el sistema de archivos
    app.config['SECRET_KEY'] = '123'  

    # Inicializa MySQL con la aplicación
    mysql.init_app(app)

    # Inicializa Flask-Session con la aplicación
    Session(app)

    # Registrar el Blueprint del controlador de usuario
    from controllers.UserController import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')
    # Registrar el Blueprint del controlador de artista
    from controllers.ArtistaController import artista_bp
    app.register_blueprint(artista_bp, url_prefix='/artistas')
    # Registrar el Blueprint del controlador de sede
    from controllers.SedeController import sede_bp
    app.register_blueprint(sede_bp, url_prefix='/sedes')
    # Registrar el Blueprint del controlador de boleto
    from controllers.BoletoController import boleto_bp
    app.register_blueprint(boleto_bp, url_prefix='/boletos')
    # Registrar el Blueprint del controlador de evento
    from controllers.EventoController import evento_bp
    app.register_blueprint(evento_bp, url_prefix='/eventos')


    return app

if __name__ == '__main__':
    app = create_app()

    #ruta al certificado y la llave
    cert = 'certificado.crt'
    key = 'clave_privada.key'
    app.run(debug=True)

    if not os.path.exists(cert) or not os.path.exists(key):
        print("No se encontraron el certificado y la clave privada.")
    else:
        # Ejecutar la aplicación con SSL habilitado
        app.run(debug=True, ssl_context=(cert, key))
