estados = ["Acre","Alagoas","Amapá","Amazonas","Bahia","Ceará","Distrito Federal","Espírito Santo","Goiás","Maranhão","Mato Grosso","Mato Grosso do Sul","Minas Gerais","Pará","Paraíba","Paraná","Pernambuco","Piauí","Rio de Janeiro","Rio Grande do Norte","Rio Grande do Sul","Rondônia","Roraima","Santa Catarina","São Paulo","Sergipe","Tocantins"]

estados_siglas = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

numeros = [3,5,9,32,12,11,9,54, 9]

numeros.append(100)
print(numeros)
print(numeros[4])
print (estados[11])
print(numeros.count(9))
print(sum(numeros))

'''
pesquisar = input('Qual estado deseja localizar? ')
indice = estados.index(pesquisar)
print(f'O estado {pesquisar} está na posição {indice}')
'''
