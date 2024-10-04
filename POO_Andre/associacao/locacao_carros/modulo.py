class Carro:
    def __init__(self, modelo, cor):
        self.__modelo = modelo
        self.__cor = cor
        self.carros_disponiveis = []

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, value):
        self.modelo = value

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, value):
        self.__cor = value
        
    def incluir_carro(self,carro):
        if carro not in self.carros_disponiveis:
            self.carros_disponiveis.append(carro)
            
    def listar_carros(self):
        for carro in self.carros_disponiveis:
            print(f'{carro.modelo} - {carro.cor}')
            
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.escolha = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    def escolher_carro(self, carro):
        self.escolha.append(carro)
    
    def consultar_escolha(self, cliente):
        return self.escolha
        
        

    