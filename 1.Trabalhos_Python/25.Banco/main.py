
'''
Crie um app de uma instituição bancária. O usuário poderá:

- Criar uma conta.
- Consultar os dados pessoais da conta.
- Alterar os dados pessoais da conta.
- Excluir a conta.

Com a conta criada, o usuário poderá realizar as seguintes operações:

- Consultar o saldo da conta.
- Depositar valor na conta.
- Sacar valor na conta.
- Sair do programa.

'Endereco','Telefone','CPF','E-mail', 'Conta'

'''

clientes = []

contas = []

chave_pessoa = ('Nome', 'Senha')

chave_conta = ('Conta', 'Saldo')

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
        case '1':
            novo_cliente = {}
            for chave in chave_pessoa:
                novo_cliente[chave] = input(f'{chave}: ')
            clientes.append(novo_cliente)            
            continue

        case '2':
            for i, cliente in enumerate(clientes):
                print(f'Cliente {i} ' + '-'*50)
                for chave in chave_pessoa:
                    print(f'{chave} - {cliente[chave]}')
            break
        
        case '3':
            cc = 0
            conta = input('Para qual cliente deseja abrir conta?')
            if conta in clientes[nome]:
                conta_numero = cc + 1
                