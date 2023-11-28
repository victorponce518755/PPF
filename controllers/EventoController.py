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
            'fecha': str(evento.fecha),  
            'hora': str(evento.hora),    
            'cantidadBoletosNormales': evento.cantidadBoletosNormales,
            'cantidadBoletosVip': evento.cantidadBoletosVip
        }
        return jsonify(evento_dict)
    else:
        return jsonify({'message': 'Evento not found'}), 404

#traer todos los eventos y que si no hay eventos, regrese un mensaje
@evento_bp.route('/evento', methods=['GET'])
def get_all_eventos():
    evento_service = EventoServices(mysql)
    eventos = evento_service.get_all_eventos()
    if eventos:
        eventos_dict = []
        for evento in eventos:
            evento_dict = {
                'idEvento': evento.idEvento,
                'idArtista': evento.idArtista,
                'nombre': evento.nombre,
                'descripcion': evento.descripcion,
                'idSede': evento.idSede,
                'fecha': str(evento.fecha),  
                'hora': str(evento.hora),    
                'cantidadBoletosNormales': evento.cantidadBoletosNormales,
                'cantidadBoletosVip': evento.cantidadBoletosVip
            }
            eventos_dict.append(evento_dict)
        return jsonify(eventos_dict)
    else:
        return jsonify({'message': 'No hay eventos'}), 404


