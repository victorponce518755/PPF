from models.ModelBoleto import ModelBoleto
from entities.boleto import Boleto

class BoletoServices:
    def __init__(self, mysql):
        self.model_boleto = ModelBoleto(mysql)

    def create_boleto(self, boleto_data):
        boleto = Boleto(None, boleto_data['idEvento'], boleto_data['idUsuario'], boleto_data['asiento'], boleto_data['tipoAsiento'], boleto_data['precio'])
        self.model_boleto.create_boleto(boleto)

    def get_boleto(self, boleto_id):
        return self.model_boleto.get_boleto(boleto_id)
    
    def get_boletos_byUserId(self, user_id):
        return self.model_boleto.get_boletos_byUserId(user_id)
    
    def get_allBoletos(self):
        return self.model_boleto.get_allBoletos()
    
