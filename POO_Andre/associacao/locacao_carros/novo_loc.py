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
        self.__modelo = value

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, value):
        self.__cor = value

    def incluir_carro(self, carro):
        if carro not in self.carros_disponiveis:
            self.carros_disponiveis.append(carro)

    def listar_carros(self):
        # Exibe a lista com a posição (índice) dos carros
        for idx, carro in enumerate(self.carros_disponiveis):
            print(f'{idx + 1}. {carro.modelo} - {carro.cor}')


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

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


# Inicialização do cliente
p1 = Cliente('', '')
p1.nome = input("Nome do cliente: ")
p1.cpf = input("CPF: ")

# Inicialização de um objeto Carro com uma lista de carros
carro_gerente = Carro('', '')

# Cadastro de 5 carros
for i in range(5):
    c = Carro('', '')
    c.modelo = input(f"Modelo do carro {i + 1}: ")
    c.cor = input(f"Cor do carro {i + 1}: ")

    # Inclui o carro na lista
    carro_gerente.incluir_carro(c)

# Exibe a lista de carros cadastrados
print("\nCarros disponíveis:")
carro_gerente.listar_carros()

# Permitir que o cliente escolha um carro
escolha = int(input("\nEscolha um carro pelo número: ")) - 1

# Verifica se a escolha é válida
if 0 <= escolha < len(carro_gerente.carros_disponiveis):
    carro_escolhido = carro_gerente.carros_disponiveis[escolha]
    
    # Imprime o nome do cliente, CPF e o carro escolhido
    print(f"\nCliente: {p1.nome}, CPF: {p1.cpf}")
    print(f"Carro escolhido: {carro_escolhido.modelo} - {carro_escolhido.cor}")
else:
    print("Escolha inválida!")
