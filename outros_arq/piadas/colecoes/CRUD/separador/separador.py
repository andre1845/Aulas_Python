nome = input("Digite o nome : ")

# separar as palavras do nome
nome_completo = nome.split(' ')  # entre parenteses vai o separador

# capitular as palavras
nome1 = ""
for parte_nome in nome_completo:
    print(parte_nome.capitalize())
    nome1 = nome1 + parte_nome.capitalize()
    
print(nome1)

nome2 = '_'.join(nome_completo)

print(nome2)