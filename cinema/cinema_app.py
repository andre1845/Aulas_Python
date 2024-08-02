
while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    if idade >= 18:
        idade_grupo = 3
    elif idade <18 and idade >=14:
        idade_grupo = 2
    else:
        idade_grupo = 1
        
    print('Qual filme deseja assistir ?')
    print('Sala 1: Star Wars - O império contra-ataca (livre)')
    print('Sala 2: O silencio dos inocentes (14 anos)')
    print('Sala 3: Hot Star (18 anos)')
    print('Sala 4: Meu malvado favorito (livre)')
    print('Sala 5: Star Trek - Into the darkness (14 anos)')

    opcao = int(input('Escolha sua sala: '))

    match opcao:
        case 2|5:
            if idade_grupo == 1:
                ingresso = 'N'
            else:
                ingresso = 'S'
        case 3:
            if idade_grupo < 3:
                ingresso = 'N'
            else:
                ingresso = 'S'
        case 1|4:
            ingresso = 'S'
        case _:
            print('Opção inválida')
            ingresso = 'N'
    if ingresso == 'S':
        print(f'Ingresso para a sala {opcao}.')
    else:
        print(f'Você não tem idade para entrar na sala {opcao}.')
        print('Escolha outra sala ou vá embora.')

    continuar = input('Deseja escolhar outra sala (s/n)?')
    if continuar.lower() == "s" :
        continue
    else:
        break


