from flask import Blueprint, request, jsonify, session
from app import mysql  # Importa la instancia de MySQL desde app
from services.UserServices import UserServices


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_service = UserServices(mysql)  # Pasa la instancia de MySQL al servicio
    user_service.create_user(user_data)
    return jsonify({'message': 'User created successfully'})

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user_service = UserServices(mysql)  # Pasa la instancia de MySQL al servicio
    user = user_service.get_user_profile(user_id)

    if user:
        user_dict = {
            'id': user.idUsuario,
            'nombre': user.nombre,
            'correo': user.correo
        }
        print(user_dict)
        return jsonify(user_dict)
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    

@user_bp.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()
    user_service = UserServices(mysql)

    # Realiza la lógica de inicio de sesión
    user = user_service.login_user(login_data['correo'], login_data['password'])

    if user:

        # Guarda el usuario en la sesión
        session['user_id'] = user.idUsuario
        session['nombre'] = user.nombre
        session['correo'] = user.correo
        # Usuario autenticado, puedes generar un token de autenticación si es necesario.
        # Luego, puedes devolver la respuesta apropiada, como un token de autenticación y
        # otros detalles del usuario.
        response = {
            'message': 'Inicio de sesión exitoso',
            'user_id': user.idUsuario,
            'nombre': user.nombre,
            'correo': user.correo,
            'token': 'tu_token_de_autenticación'  # Genera un token si es necesario
        }
        return jsonify(response)
    else:
        # Usuario no autenticado, devuelve una respuesta de error apropiada.
        return jsonify({'message': 'Inicio de sesión fallido'}), 401  # 401: Unauthorized
