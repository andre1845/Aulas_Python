var = input('Digite a variável.')
result = '-'.join(var)
print(result)

var1 = input('Var 1: ')
var2 = input('Var 2: ')
alfa = f'{var1}{var2}'
bravo = f'{var2}{var1}{var2}'
print(alfa)
print(bravo)
print(bravo[-3]+bravo[-2])
print(bravo[-2]+bravo[-1])