


def somar (x, y):
    soma = x+y
    return soma


multiplicar = lambda x,y: x * y

x = int(input('Valor de X : '))
y = int(input('Valor de y : '))

print (f'Soma = {somar(x,y)}')
print (f'Multiplicação = {multiplicar(x,y)}')