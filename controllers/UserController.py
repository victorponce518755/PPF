from flask import Blueprint, request, jsonify, session
from app import mysql  # Importa la instancia de MySQL desde app
from services.UserServices import UserServices
from xml.etree import ElementTree as ET


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_service = UserServices(mysql)  
    user_service.create_user(user_data)
    return jsonify({'message': 'User created successfully'})

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user_service = UserServices(mysql)  
    user = user_service.get_user_profile(user_id)

    if user:
        user_dict = {
            'id': user.id,
            'nombre': user.name,
            'username': user.username,
            'usuario creado': user.created_at,
            'usuario actualizado': user.updated_at
        }
        print(user_dict)
        return jsonify(user_dict)
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404
       

@user_bp.route('/login1', methods=['POST'])
def login1():
    login_data = request.get_json()
    user_service = UserServices(mysql)

    # Realiza la lógica de inicio de sesión
    user = user_service.login_user(login_data['correo'], login_data['password'])

    if user:

        
        session['user_id'] = user.id
        session['nombre'] = user.name
        session['username'] = user.username
        
        response = {
            'message': 'Inicio de sesión exitoso',
            'user_id': user.id,
            'nombre': user.nombre,
            'correo': user.correo,
            'token': 'tu_token_de_autenticación'  
        }
        return jsonify(response)
    else:
        
        return jsonify({'message': 'Inicio de sesión fallido'}), 401  


@user_bp.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()
    user_service = UserServices(mysql)

    
    user = user_service.login_user2(login_data['username'], login_data['password'])

    if user:

        
        response = {
            'message': 'Inicio de sesión exitoso',
            'user_id': user.id,
            'nombre': user.name,
            'username': user.username,
            'admin': user.is_admin,
            
        }
        return jsonify(response)
    else:
        
        return jsonify({'message': 'Inicio de sesión fallido'}), 401  