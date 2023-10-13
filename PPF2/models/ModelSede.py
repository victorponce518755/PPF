from entities.sede import Sede
from flask_mysqldb import MySQL

class ModelSede:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_sede(self, sede):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO Sede (nombre, capacidad, ubicacion) VALUES (%s, %s, %s)',
            (sede.nombre, sede.capacidad, sede.ubicacion)
        )
        self.mysql.connection.commit()
        cursor.close()

    def get_sede(self, sede_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT Sede.idSede, Sede.nombre, Sede.capacidad, Sede.ubicacion FROM Sede WHERE idSede = %s', (sede_id,))
        sede_data = cursor.fetchone()
        cursor.close()

        if sede_data:
            sede = Sede(sede_data[0], sede_data[1], sede_data[2], sede_data[3])
            return sede
        else:
            return None

