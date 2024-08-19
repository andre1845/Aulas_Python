print('Alô, mundo')
# comentario
'''
comentario de bloco
'''
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Exemplo de uso:
limpar_tela()
print('hello word')
print('teste')
limpar_tela()
