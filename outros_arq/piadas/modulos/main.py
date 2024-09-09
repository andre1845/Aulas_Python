import cinematica as cn
# from cinematica import* - maneira para importar tudo de cinematica e nao precisar citar o arquivo na chamada da funcao

while True:
    cn.menu()
    opcao = input('Escolha sua opcao ')

    match opcao:
        
        case '1':
            m = float(input('massa em kg: ').replace(',','.'))
            h = float(input('altura em m: ').replace(',','.'))
            print(f'EP: {cn.calcular_ep(m,h):,.2f} J.')
            print('-'*50)
            continue
        
        case '2':
            
            m = float(input('massa em kg: ').replace(',','.'))
            v = float(input('velocidade em m/s: ').replace(',','.'))
            print(f'EC: {cn.calcular_ec(m,h):,.2f} J.')
            print('-'*50)
            continue
        
        case '3':
            distancia = float(input('Digite a distância da viagem: '))
            combustivel = float(input('Digite o valor do litro do combustível: '))
            veloc_media = float(input('Digite a velocidade média da viagem: '))
            consumo_carro = float(input('Digite o consumo médio em Km/l: '))
            
            tempo_gasto = cn.tempo_viagem(distancia, veloc_media)
            combustivel_total = cn.consumo(distancia, consumo_carro)
            valor_gasto = cn.custo_viagem(combustivel, combustivel_total)
            
            print(' ')
            print(f'A viagem vai durar {tempo_gasto} horas')
            print(f'A viagem vai custar {valor_gasto} reais')
            print(f'A viagem vai consumir {combustivel_total} litros de combustivel')
            print('-' * 50)
            continue
        case _:
            print('FINAL')
            break
            