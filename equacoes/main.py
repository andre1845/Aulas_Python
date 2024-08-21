import formulas as frm


if __name__ == '__main__':
    while True:
        frm.mostrar_menu()
        opcao = input('Escolha a opcao')
        match opcao:
            case '1':
                a = float(input('Valor de "a": ').replace(',','.'))
                b = float(input('Valor de "b": ').replace(',','.'))
                print(f'Valor de "X" = {frm.calc_grau_1(a,b)}')
                
            case '2':
                a = float(input('Valor de "a": ').replace(',','.'))
                b = float(input('Valor de "b": ').replace(',','.'))
                c = float(input('Valor de "c": ').replace(',','.'))
                print(frm.calc_grau_2(a,b,c))
                
            case '3':
                print('FIM')
                break
                
            case _:
                print('Opcao invalida')
                continue
                