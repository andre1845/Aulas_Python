x = int(input('primeiro numero: '))
y = input('segundo numero: ')

try:
    multiplicacao = x * int(y)
    print(multiplicacao)
except:
    print("Deu errado")