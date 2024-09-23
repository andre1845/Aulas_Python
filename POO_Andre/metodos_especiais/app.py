from modulo import *

alfa = input('Nome: ')
print(alfa)

bravo = Pessoa('',0,'')
bravo.nome = input('Nome B: ')
bravo.idade = input('idade B: ')
bravo.email = input('email B: ')

print(len(bravo.nome))
print(len(alfa))
print(bravo.nome)
print(str(bravo))
print(repr(bravo))