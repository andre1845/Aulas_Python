# Declaração de variáveis

var1 = 12
numeros = [2,4,6,8,23]
'''
print(numeros[1])
print(numeros[-1])
print(numeros[-2])
'''
nome = 'amanda'

# print(nome)
# print(nome[1])
# print(nome[-1])
# print(len(numeros))

palavra = "arara"

print('sim') if len(palavra) >=8 else print("nao")

nome: str = "Andre"

for i in range(1,10,2):
    print(i)

print('Nome: ' + nome + '.')
# O sinal + serve para concatenar APENAS string

nome2 = 'Andre'
idade = 48

print('Nome: '+nome2+' idade: '+str(45))