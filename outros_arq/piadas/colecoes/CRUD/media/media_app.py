import os

os.system('cls')

numeros = [10, 5, 7, 4, 6, 3, 8, 10, 7]

numeros.sort(reverse=True)

for numero in numeros:
    print(numero, end=' ') # o end= ' ' troca a quebra de linha pelo caracter que está entre aspas
soma = sum(numeros)
print(f'\nSoma = {soma}')

media = (soma)/(len(numeros))
print(f'\nMedia = {media:,.2f}')
