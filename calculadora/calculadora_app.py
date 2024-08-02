while True:

    numero_1 = float(input('Numero 1: '))
    operacao = input('Operação (+, -, *, /) : ')
    numero_2 = float(input('Numero 2: '))

    match operacao:
        case '+':
            result = numero_1 + numero_2
        case '-':
            result = numero_1 - numero_2
        case '*':
            result = numero_1 * numero_2
        case '/':
            result = numero_1 / numero_2
        case _:
            print('Opção invalida')
            result = 0

    print(f'{numero_1} {operacao} {numero_2} = {result}')
    
    continuar = input('Outra opeção (s/n)?')
    if continuar.lower() == "s":
        continue
    else:
        break