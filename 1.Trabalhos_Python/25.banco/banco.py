clientes = []
contas = []

chave_pessoa = ('Nome','CPF', 'E-mail', 'Senha')
chave_conta = ('Cliente','Conta', 'Saldo', 'Data de Abertura')

def numero_positivo(mensagem):
    while True:
        valor = input(mensagem)
        try:
            valor_float = float(valor)
            if valor_float > 0:
                return valor_float
            else:
                print("O valor deve ser maior que 0. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
            continue


def menu():
    print('.' * 50)
    print('1 - Cadastrar cliente')
    print('2 - Consultar dados de cliente')
    print('3 - Alterar dados de cliente')
    print('4 - Abrir conta corrente')
    print('5 - Consultar saldo')
    print('6 - Fazer depósito')
    print('7 - Sacar valor')
    print('9 - Encerrar programa')
    print('.' * 50)

while True:
    menu()
    opcao = input('Digite a opcao: ')
    
    match opcao:
        case '1':  # Cadastrar cliente
            novo_cliente = {}
            for chave in chave_pessoa:
                novo_cliente[chave] = input(f'{chave}: ')
            clientes.append(novo_cliente)
            print("Cliente cadastrado com sucesso!")
            continue
        
        case '2':  # Consultar dados de cliente
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for i, cliente in enumerate(clientes, start=1):
                    print(f'Cliente {i} ' + '-' * 50)
                    
                    # Exibe os dados do cliente
                    for chave in chave_pessoa:
                        print(f'{chave}: {cliente[chave]}')
                    
                    # Encontra e exibe as contas associadas ao cliente
                    contas_cliente = [conta for conta in contas if conta['Cliente'] == cliente['Nome']]
                    
                    if contas_cliente:
                        print('Contas: _________')
                        for conta in contas_cliente:
                            for chave in chave_conta[1:]:  # Pula a chave 'Cliente' na exibição
                                if chave == 'Saldo':
                                    print(f" --> {chave}: {conta[chave]:.2f}")
                                else:
                                    print(f' --> {chave}: {conta[chave]}')
                                    
                            print('-' * 50)
                    else:
                        print('Nenhuma conta encontrada para este cliente.')
                    print('-' * 50)
            continue

        
        case '3':  # Alterar dados de cliente
            nome_alterar = input('Digite o nome do cliente que deseja alterar: ')
            cliente_encontrado = False
            for cliente in clientes:
                if cliente['Nome'] == nome_alterar:
                    cliente_encontrado = True
                    for chave in chave_pessoa:
                        novo_valor = input(f'Digite o novo(a) {chave} (ou pressione Enter para manter o atual): ')
                        if novo_valor:
                            if chave == 'Nome':
                                for conta in contas:
                                    if conta['Cliente'] == nome_alterar:
                                        conta['Cliente'] = novo_valor
            
                            cliente[chave] = novo_valor
                    print("Dados do cliente alterados com sucesso.")
                    break
            if not cliente_encontrado:
                print('Cliente não encontrado.')
            continue
        
        case '4':  # Abrir conta corrente
            nome_cliente = input('Digite o nome do cliente para abrir uma conta: ')
            cliente_encontrado = False
            for cliente in clientes:
                if cliente['Nome'] == nome_cliente:
                    cliente_encontrado = True
                    nova_conta = {}
                    nova_conta['Cliente'] = nome_cliente

                    while True:
                        nova_conta['Conta'] = input('Número da conta: ')
                        conta_existe = any(conta['Conta'] == nova_conta['Conta'] for conta in contas)
                        if conta_existe:
                            print('Conta já em uso. Escolha outro número.')
                        else:
                            break
                    try:
                        nova_conta['Saldo'] = numero_positivo('Saldo inicial: ')
                    except:
                        print('Valor inválido! -> Saldo inicial = 0')
                        nova_conta['Saldo'] = 0
                        
                    nova_conta['Data de Abertura'] = input('Data de Abertura (DD/MM/AAAA): ')
                    contas.append(nova_conta)
                    print("Conta aberta com sucesso!")
                    break
            
            if not cliente_encontrado:
                print('Cliente não encontrado. Por favor, cadastre o cliente primeiro.')
            continue


        case '5':  # Consultar saldo
            conta_consultar = input('Digite o número da conta para consultar o saldo: ')
            conta_encontrada = False
            for conta in contas:
                if conta['Conta'] == conta_consultar:
                    conta_encontrada = True
                    print(f"Saldo da conta {conta_consultar}: R$ {conta['Saldo']:.2f}")
                    break
            if not conta_encontrada:
                print('Conta não encontrada.')
            continue

        case '6':  # Fazer depósito
            conta_depositar = input('Digite o número da conta para depósito: ')
            conta_encontrada = False
            for conta in contas:
                if conta['Conta'] == conta_depositar:
                    conta_encontrada = True
                    valor_deposito = numero_positivo('Digite o valor do depósito: ')
                    conta['Saldo'] += valor_deposito
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
                    break
            if not conta_encontrada:
                print('Conta não encontrada.')
            continue

        case '7':  # Sacar valor
            conta_sacar = input('Digite o número da conta para saque: ')
            conta_encontrada = False
            for conta in contas:
                if conta['Conta'] == conta_sacar:
                    conta_encontrada = True
                    valor_saque = numero_positivo('Digite o valor do saque: ')
                    if valor_saque > conta['Saldo']:
                        print("Saldo insuficiente para o saque.")
                    else:
                        conta['Saldo'] -= valor_saque
                        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                    break
            if not conta_encontrada:
                print('Conta não encontrada.')
            continue

        case '9':  # Encerrar programa
            print('Encerrando o programa...')
            break

        case _:  # Opção inválida
            print('Opção inválida, tente novamente.')
            continue

                