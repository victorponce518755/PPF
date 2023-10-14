from flask import Blueprint, request, jsonify, session
from app import mysql
from services.BoletoServices import BoletoServices

boleto_bp = Blueprint('boleto_bp', __name__)

@boleto_bp.route('/boleto', methods=['POST'])
def create_boleto():
    if 'user_id' not in session:
        return jsonify({'message': 'Usuario no autenticado'}), 401

    user_id = session['user_id']
    boleto_data = request.get_json()
    boleto_data['idUsuario'] = user_id

    boleto_service = BoletoServices(mysql)
    boleto_service.create_boleto(boleto_data)
    return jsonify({'message': 'Boleto creado exitosamente'})

@boleto_bp.route('/boleto/<int:boleto_id>', methods=['GET'])
def get_boleto(boleto_id):
    boleto_service = BoletoServices(mysql)
    boleto = boleto_service.get_boleto(boleto_id)

    if boleto:
        boleto_dict = {
            'idBoleto': boleto.idBoleto,
            'idUsuario': boleto.idUsuario,
            'idEvento': boleto.idEvento,
            'tipoAsiento': boleto.tipoAsiento,
            'asiento': boleto.asiento,
            'precio' : boleto.precio

        }
        return jsonify(boleto_dict)
    else:
        return jsonify({'message': 'Boleto no encontrado'}), 404