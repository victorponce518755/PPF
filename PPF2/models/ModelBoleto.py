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
