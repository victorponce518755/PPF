from flask import Blueprint, request, jsonify, session
from app import mysql
from services.BoletoServices import BoletoServices

boleto_bp = Blueprint('boleto_bp', __name__)

@boleto_bp.route('/boleto', methods=['POST'])
def create_boleto():

    boleto_data = request.get_json()
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
    
@boleto_bp.route('/boleto/user/<int:user_id>', methods=['GET'])
def get_boletos_by_user_id(user_id):
    boleto_service = BoletoServices(mysql)
    boletos = boleto_service.get_boletos_byUserId(user_id)

    if boletos:
        boletos_list = []
        for boleto in boletos:
            boleto_dict = {
                'idBoleto': boleto.idBoleto,
                'idUsuario': boleto.idUsuario,
                'idEvento': boleto.idEvento,
                'tipoAsiento': boleto.tipoAsiento,
                'asiento': boleto.asiento,
                'precio': boleto.precio
            }
            boletos_list.append(boleto_dict)

        return jsonify(boletos_list)
    else:
        return jsonify({'message': 'No se encontraron boletos para el usuario'}), 404
