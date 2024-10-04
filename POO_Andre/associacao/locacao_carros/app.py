from modulo import *

carro_modelo = Carro('','')
p1 = Cliente('','')
p1.nome = input("Nome do cliente: ")
p1.cpf = input("CPF: ")

while True:
    c = Carro('','')
    c.modelo = input("Modelo do carro: ")
    c.cor = input("Cor do carro: ")
    carro_modelo.incluir_carro(c)
    
    opcao = input('Continuar? s/n ')
    if opcao.lower() != 'n':
        continue
    else:
        break
carro_modelo.listar_carros()
print(' ')
while True:
    escolha = int(input("Escolha seu carro: "))
    if escolha < 1 or escolha > 5:
        continue
    else:
        break
    


