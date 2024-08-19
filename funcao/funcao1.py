def entrada(var):
    print(f'Enrada {var} do bloco de código')
    print(f'Funcao {var} executando')
    try:
        x = int(var) * 2
        print(x)
    except:
        print(var)

nome = input('Nome? ')    
entrada(nome)