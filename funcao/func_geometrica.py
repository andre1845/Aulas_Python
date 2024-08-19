def mostra_menu():
    print('1 - Calcular quadrilatero')
    print('2 - Calcular triangulo')
    print('3 - Calcular circulo')
    print('4 - Sair')

def quadrilatero(base, altura):
    result = base * altura
    return result

def triangulo(base, altura):
    result = base * (altura / 2)
    return result

def circulo(raio):
    result = 3.14 * (raio**2)
    return result

# programa principal (MAIN)
while True:
    mostra_menu()
    opcao = input('opcao? ')

    match opcao:
        
        case '1':
            b = float(input("Digite a base: "))
            a = float(input("Digite a altura: "))
            print(f'Area do quadrilatero = {quadrilatero(b,a)}')
            continue
        case '2':
            b = float(input("Digite a base: "))
            a = float(input("Digite a altura: "))
            print(f'Area do triangulo = {triangulo(b,a)}')
            continue
        case '3':
            r = float(input("Digite o raio: "))
            print(f'Area do circulo = {circulo(r)}')
            continue
        case _:
            print('FINAL')
            break
        




