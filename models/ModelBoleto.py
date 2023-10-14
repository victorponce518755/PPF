from entities.boleto import Boleto
from flask_mysqldb import MySQL

class ModelBoleto:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_boleto(self, boleto):
        cursor = self.mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO Boletos (idEvento, idUsuario, asiento, tipoAsiento, precio) VALUES (%s, %s, %s, %s, %s)',
            (boleto.idEvento, boleto.idUsuario, boleto.asiento, boleto.tipoAsiento, boleto.precio)
        )
        self.mysql.connection.commit()
        cursor.close()

    def get_boleto(self, boleto_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM Boletos WHERE idBoleto = %s', (boleto_id,))
        boleto_data = cursor.fetchone()
        cursor.close()

        if boleto_data:
            boleto = Boleto(boleto_data[0], boleto_data[1], boleto_data[2], boleto_data[3], boleto_data[4], boleto_data[5])
            return boleto
        else:
            return None
