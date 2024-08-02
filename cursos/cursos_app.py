nome = input("Qual seu nome?")
opcao = input('\nDigite a opção')

match int(opcao):
    case 1:
        print(f'{nome} se matriculou no Op Micro')
    case 2:
        print(f'{nome} se matriculou no Java')
    case 3:
        print(f'{nome} se matriculou no Python')
    case 4:
        print(f'{nome} se matriculou no Front-End')
    case 5:
        print(f'{nome} se matriculou no manutenção')
    case _:
        print('Opcao invalida')