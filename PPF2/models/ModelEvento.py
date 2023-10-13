from entities.evento import Evento
from flask_mysqldb import MySQL

class ModelEvento:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_evento(self, evento):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO Eventos (idArtista, nombre, descripcion, idSede, fecha, hora, cantidadBoletosNormales, cantidadBoletosVip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (evento.idArtista, evento.nombre, evento.descripcion, evento.idSede, evento.fecha, evento.hora, evento.cantidadBoletosNormales, evento.cantidadBoletosVip)
        )
        self.mysql.connection.commit()
        cursor.close()

    def get_evento_info(self, evento_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT Eventos.idEvento, Eventos.idArtista, Eventos.nombre, Eventos.descripcion, Eventos.idSede, Eventos.fecha, Eventos.hora, Eventos.cantidadBoletosNormales, Eventos.cantidadBoletosVip FROM Eventos WHERE idEvento = %s', (evento_id,))
        evento_data = cursor.fetchone()
        cursor.close()

        if evento_data:
            evento = Evento(evento_data[0], evento_data[1], evento_data[2], evento_data[3], evento_data[4], evento_data[5], evento_data[6], evento_data[7], evento_data[8])
            return evento
        else:
            return None
