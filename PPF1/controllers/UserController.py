from flask import Blueprint, request, jsonify
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
            'username': user.username,
            'email': user.email
        }
        print(user_dict)
        return jsonify(user_dict)
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404
