import os
import time

numero = int(input('Digite o inicio: '))
final = int(input('Digite o final: '))
while numero >= final:
    os.system('cls')
    print('\nContagem Regressiva: ')
    print(f'{numero}.....')
    numero -= 1
    time.sleep(1)
    # esse TIME.SLEEP vem da biblioteca TIME e faz um "pause" em segundos com o tempo definido entre parenteses
print('Acabou!')
    