class Carro:
    def __init__(self, modelo, cor):
        self.__modelo = modelo
        self.__cor = cor

    @property
    def _modelo(self):
        return self.__modelo

    @_modelo.setter
    def _modelo(self, value):
        self.__modelo = value

    @property
    def _cor(self):
        return self.__cor

    @_cor.setter
    def _cor(self, value):
        self.__cor = value
        
        
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

        

    