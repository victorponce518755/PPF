from entities.artista import Artista
from flask_mysqldb import MySQL

class ModelArtista:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_artista(self, artista):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO Artista (nombre, generoMusical) VALUES (%s, %s)',
            (artista.nombre, artista.generoMusical)
        )
        self.mysql.connection.commit()
        cursor.close()


    def get_artista(self, artista_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM Artista WHERE idArtista = %s', (artista_id,))
        artista_data = cursor.fetchone()
        cursor.close()

        if artista_data:
            artista = Artista(artista_data[0], artista_data[1], artista_data[2])
            return artista
        else:
            return None
