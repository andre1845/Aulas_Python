import modulo as md

if __name__ == "__main__":
    
    contas_abertas = []
    
    def menuConta():
        print('1 - Consultar Saldo')
        print('2 - Sacar')
        print('3 - Depositar')
        print('4 - Sair')
        
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
   
    
    
    # Criando um gerador de contas
    gerador = md.GeradorDeContas()
    
    while True:
    
        cc = md.ContaCorrente('','', '', '', 0)
        
        cc.nome = input('Qual o nome?')
        cc.cpf = input('Qual o CPF?')
        cc.agencia = '1001'
        cc.conta = gerador.gerar_numero_conta()
        
        contas_abertas.append(cc)
        
        opcao = input('Continuar? s/n ')
        if opcao.lower() != 's':
            break
        
    # Exibir todas as contas cadastradas
    print("Contas cadastradas:")
    for conta in contas_abertas:
        print(f'Conta Corrente: {conta.conta} - Cliente: {conta.nome}')

    while True:
    # Buscar uma conta específica
        numero_conta = input("\nDigite o número da sua conta: ")

        # Procurar a conta correspondente
        conta_encontrada = None
        for conta in contas_abertas:
            if conta.conta == int(numero_conta):
                conta_encontrada = conta
                break
            
        if conta_encontrada is None:
            print(f"Conta {numero_conta} não encontrada.")
        else:      
            while True:
                menuConta()
                opcaoConta = input('Digite sua opção: ')
                
                match opcaoConta:
                    case '1':
                        saldo = conta_encontrada.consultar_saldo()
                        print(f'Conta {conta_encontrada.conta} - saldo: {saldo:.2f}')
                        print('.'*50)
                        continue
                    case '2':
                        valor = numero_positivo('Digite o valor a ser sacado: ')
                        conta_encontrada.fazer_saque(valor)
                        continue
                    case '3':
                        valor = numero_positivo('Digite o valor a ser depositado: ')
                        conta_encontrada.fazer_deposito(valor)
                        continue
                    case '4':
                        print(f'Fim da operação na conta: {conta_encontrada.conta}')
                        break
                    case _:
                        print('Opção inválida')
                        continue
        opcao = input('Deseja consultar outra conta? s/n ')
        if opcao.lower() != 's':
            break
       
    print('-'*50)
    print(' ---  CONTAS ABERTAS  ---')
    for conta in contas_abertas:
        print('-'*50)
        print(f'Cliente: {conta.nome}')
        print(f'CPF: {conta.cpf}')
        print(f'Agencia: {conta.agencia}')
        print(f'Conta Corrente: {conta.conta}')
        print(f'Saldo: {conta.saldo:.2f}')
    
    
        '''
            
            # Procurar a conta correspondente
    conta_encontrada = None
    for conta in contas_abertas:
        if conta.conta == int(numero_conta):
            conta_encontrada = conta
            break  # Saia do loop quando a conta for encontrada
        else:
            print(f"Conta {numero_conta} não encontrada.")
            
            '''