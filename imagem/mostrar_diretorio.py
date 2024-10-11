import os

# Obter o diretório do arquivo atual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Imprimir o diretório no terminal
print("O diretório do arquivo atual é:", current_directory)


# Definir o diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Nome da imagem
imagem = input("Escolha a imagem ")

# Criar o caminho completo para a imagem
imagem2 = os.path.join(diretorio_atual, imagem)

# Imprimir o caminho completo da imagem
print("O caminho completo da imagem é:", imagem2)
