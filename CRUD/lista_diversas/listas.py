import os
lista = []
os.system('cls')
while True:
    print('>'*20 + " MENU " + '<'*20)
    print("1 - Incluir na lista.")
    print("2 - Excluir da lista.")
    print("3 - Alterar nome da lista.")
    print("4 - Separar da lista.")
    print("5 - Localizar na lista.")
    print("6 - Imprimir lista principal ordenada.")
    print("7 - Imprimir itens retirados da lista.")
    print("8 -  e imprimir itens retirados da lista.")
    print("9 - Sair.")
    print('-' * 60)
    print(f'\n')
    
    opcao = input("Digite sua opção ")
    
    match opcao :
        case '1':
            nome = input('Nome a incluir na lista: ')
            if nome != "":
                lista.append(nome)
                print(f'{nome} incluído!')
            else:
                print('Você não dgitou nada...')
            continue
        case '2':
            nome = input('Nome a ser excluido da lista: ')
            try:
                lista.remove(nome)
                print(f'{nome} excluido!')
            except:
                print(f'{nome} não encontrado')
            finally:
                continue
        case '6':
            lista.sort()
            print('.' * 20 + 'LISTA ORDENADA' + '.'*20)
            for nome in lista:
                print(nome)
            print('-' * 50)        
            continue  
        case '9':
            print('Case 9')
            break
        case _:
            print('Opção inválida')
            continue
    