from models.ModelBoleto import ModelBoleto
from entities.boleto import Boleto

class BoletoServices:
    def __init__(self, mysql):
        self.model_boleto = ModelBoleto(mysql)

    def create_boleto(self, boleto_data):
        boleto = Boleto(None, boleto_data['idEvento'], boleto_data['idUsuario'], boleto_data['asiento'], boleto_data['tipoAsiento'], boleto_data['precio'])
        self.model_boleto.create_boleto(boleto)
