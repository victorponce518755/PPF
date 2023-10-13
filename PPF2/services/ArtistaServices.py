from models.ModelArtista import ModelArtista
from entities.Artista import Artista

class ArtistaServices:
    def __init__(self, mysql):
        self.model_artista = ModelArtista(mysql)

    def create_artista(self, artista_data):
        artista = Artista(None, artista_data['nombre'], artista_data['generoMusical'])
        self.model_artista.create_artista(artista)

    def get_artista(self, artista_id):
        return self.model_artista.get_artista(artista_id)
