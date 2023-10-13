from flask import Blueprint, request, jsonify
from app import mysql
from services.EventoServices import EventoServices

evento_bp = Blueprint('evento_bp', __name__)

@evento_bp.route('/evento', methods=['POST'])
def create_evento():
    evento_data = request.get_json()
    evento_service = EventoServices(mysql)
    evento_service.create_evento(evento_data)
    return jsonify({'message': 'Evento created successfully'})

@evento_bp.route('/evento/<int:evento_id>', methods=['GET'])
def get_evento_info(evento_id):
    evento_service = EventoServices(mysql)
    evento = evento_service.get_evento_info(evento_id)

    if evento:
        evento_dict = {
            'idEvento': evento.idEvento,
            'idArtista': evento.idArtista,
            'nombre': evento.nombre,
            'descripcion': evento.descripcion,
            'idSede': evento.idSede,
            'fecha': str(evento.fecha),  # Convierte la fecha a una cadena legible
            'hora': str(evento.hora),    # Convierte la hora a una cadena legible
            'cantidadBoletosNormales': evento.cantidadBoletosNormales,
            'cantidadBoletosVip': evento.cantidadBoletosVip
        }
        return jsonify(evento_dict)
    else:
        return jsonify({'message': 'Evento not found'}), 404
