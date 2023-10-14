from models.ModelSede import ModelSede
from entities.sede import Sede

class SedeServices:
    def __init__(self, mysql):
        self.model_sede = ModelSede(mysql)

    def create_sede(self, sede_data):
        sede = Sede(None, sede_data['nombre'], sede_data['capacidad'], sede_data['ubicacion'])
        self.model_sede.create_sede(sede)

    def get_sede_info(self, sede_id):
        return self.model_sede.get_sede(sede_id)
