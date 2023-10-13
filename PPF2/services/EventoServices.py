from models.ModelEvento import ModelEvento
from entities.evento import Evento

class EventoServices:
    def __init__(self, mysql):
        self.model_evento = ModelEvento(mysql)

    def create_evento(self, evento_data):
        evento = Evento(None, evento_data['idArtista'], evento_data['nombre'], evento_data['descripcion'], evento_data['idSede'], evento_data['fecha'], evento_data['hora'], evento_data['cantidadBoletosNormales'], evento_data['cantidadBoletosVip'])
        self.model_evento.create_evento(evento)

    def get_evento_info(self, evento_id):
        return self.model_evento.get_evento_info(evento_id)
