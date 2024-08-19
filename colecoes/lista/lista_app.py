nomes = ["Andre", "Maria", "Ricardo", "Samanta", "Rebeca"]

for nome in nomes:
    print (nome)
    
# o uso do range pressupoe um numero inteiro
# dentro do range, o segundo numero é de onde começamos e o terceiro numero é negativo para indicar que vai iterar ao contrario

for i in range(len(nomes)-1,-1,-1):
    print(nomes[i])

for i in range(len(nomes)):
    print(f'{i + 1} nome: {nomes[i]}')
    print(f'{i + 1} nome: {nome[i]}')

print(nomes[0][-3])

print(type(nomes))