def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
if  __name__ == '__main__':
    while True:
        try:
            n = int(input('Informe um número : '))
            if n >= 0:
                print(f'O fatorial de {n} é {fatorial(n)}')
            else:
                print(f'Não existe fatorial de {n}')
        except:
            print('Não fo possível calcular o fatorial')
        opcao = input('Continuar? s/n : ')
        if opcao != 'n':
            continue
        else:
            break