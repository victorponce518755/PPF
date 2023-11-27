from flask import Blueprint, request, jsonify
from app import mysql
from services.SedeServices import SedeServices

sede_bp = Blueprint('sede_bp', __name__)

@sede_bp.route('/sede', methods=['POST'])
def create_sede():
    sede_data = request.get_json()
    sede_service = SedeServices(mysql)
    sede_service.create_sede(sede_data)
    return jsonify({'message': 'Sede created successfully'})

@sede_bp.route('/sede/<int:sede_id>', methods=['GET'])
def get_sede_info(sede_id):
    sede_service = SedeServices(mysql)
    sede = sede_service.get_sede_info(sede_id)

    if sede:
        sede_dict = {
            'idSede': sede.idSede,
            'nombre': sede.nombre,
            'capacidad': sede.capacidad,
            'ubicacion': sede.ubicacion
        }
        return jsonify(sede_dict)
    else:
        return jsonify({'message': 'Sede not found'}), 404
    
@sede_bp.route('/sede', methods=['GET'])
def get_all_sedes():
    sede_service = SedeServices(mysql)
    sedes = sede_service.get_all_sedes()

    if sedes:
        sedes_list = []
        for sede in sedes:
            sede_dict = {
                'idSede': sede.idSede,
                'nombre': sede.nombre,
                'capacidad': sede.capacidad,
                'ubicacion': sede.ubicacion
            }
            sedes_list.append(sede_dict)
        return jsonify(sedes_list)
    else:
        return jsonify({'message': 'No hay sedes registradas'}), 404
