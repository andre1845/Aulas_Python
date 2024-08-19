while True:
    num = int(input('Digite um numero: '))

    for i in range(num):
        print(i)
        
    continuar = input('continuar? ')
    if continuar.lower() == 's':
        continue
    else:
        break