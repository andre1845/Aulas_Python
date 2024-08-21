def mostrar_menu():
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Extrair o resto da divisão')
    print('6 - Potenciação')
    print('7 - Sair do programa')
    
somar = lambda x,y: x + y
subtrair = lambda x,y: x - y
multiplicacao = lambda x,y: x * y
divisao = lambda x,y: x / y
resto = lambda x,y: x % y
potencia = lambda x,y: x ** y
    
    # programa principal
    
if __name__ == '__main__':
    
    while True:
        mostrar_menu()
        opcao = input('Digite a operacao: ')
        
          # Se a opção não for de 1 a 7, o programa se encerra
        if opcao not in {'1', '2', '3', '4', '5', '6', '7'}:
            print('Opção inválida!')
            continue
        
        if opcao == '7':
            print('FIM')
            break
        
        x = float(input('Valor de X: '))    
        y = float(input('Valor de Y: '))    
        match opcao:
            case '1':
                print('-'*50)
                print(f'{x} + {y} = {somar(x,y)}')
                print('-'*50)
                continue
            case '2':
                print('-'*50)
                print(f'{x} - {y} = {subtrair(x,y)}')
                print('-'*50)
                continue
            case '3':
                print('-'*50)
                print(f'{x} * {y} = {multiplicacao(x,y)}')
                print('-'*50)
                continue
            case '4':
                print('-'*50)
                print(f'{x} / {y} = {divisao(x,y)}')
                print('-'*50)
                continue
            case '5':
                print('-'*50)
                print(f'Resto de {x} / {y} = {resto(x,y)}')
                print('-'*50)
                continue
            case '6':
                print('-'*50)
                print(f'{x} ** {y} = {potencia(x,y)}')
                print('-'*50)
                continue
            case _:
                print('-'*50)
                print(f'Opção inválida')
                print('-'*50)
                continue
     
                