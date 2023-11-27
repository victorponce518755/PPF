from flask import Blueprint, request, jsonify
from app import mysql
from services.ArtistaServices import ArtistaServices

artista_bp = Blueprint('artista_bp', __name__)

@artista_bp.route('/artista', methods=['POST'])
def create_artista():
    artista_data = request.get_json()
    artista_service = ArtistaServices(mysql)
    artista_service.create_artista(artista_data)
    return jsonify({'message': 'Artista creado exitosamente'})

@artista_bp.route('/artista/<int:artista_id>', methods=['GET'])
def get_artista(artista_id):
    artista_service = ArtistaServices(mysql)
    artista = artista_service.get_artista(artista_id)

    if artista:
        artista_dict = {
            'idArtista': artista.idArtista,
            'nombre': artista.nombre,
            'generoMusical': artista.generoMusical
        }
        return jsonify(artista_dict)
    else:
        return jsonify({'message': 'Artista no encontrado'}), 404
    
@artista_bp.route('/artista', methods=['GET'])
def get_all_artistas():
    artista_service = ArtistaServices(mysql)
    artistas = artista_service.get_all_artistas()

    if artistas:
        artistas_list = []
        for artista in artistas:
            artista_dict = {
                'idArtista': artista.idArtista,
                'nombre': artista.nombre,
                'generoMusical': artista.generoMusical
            }
            artistas_list.append(artista_dict)
        return jsonify(artistas_list)
    else:
        return jsonify({'message': 'No hay artistas registrados'}), 404

