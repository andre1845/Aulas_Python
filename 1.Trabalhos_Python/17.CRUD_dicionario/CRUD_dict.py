'''
Crie, em Python, um CRUD de usuários completo (Cadastrar, Pesquisar/Listar, Alterar e Excluir).
O programa deverá:

- Cadastrar usuário
- Listar todos os usuários
- Pesquisar por um usuário
- Alterar os dados do usuário
- Excluir usuário
- Sair do programa

O usuário deverá cadastrar:

- Nome completo
- Data de Nascimento
- CPF
- Profissão
- E-mail
- Endereço
- Telefone
'''
import os

clientes = []

dados = ('Nome',
'Data de Nascimento',
'CPF',
'Profissão',
'Email',
'Endereço',
'Telefone',
)
os.system('cls')
while True:
    print('>'*20 + "  CADASTRO DE CLIENTES  " + '<'*20)
    print('1 - Incluir cliente')
    print('2 - Listar clientes')
    print('3 - Alterar dados de cliente')
    print('4 - Excluir cliente')
    print('5 - Pesquisar cliente')

    opcao = input('Digite sua opção ')
    print('.'*60)

    match opcao:
        
        case '1': # INCLUIR
            novo_cliente = {}
            for chave in dados:
                novo_cliente[chave] = input(f'Digite o(a) {chave} do cliente: ')
            clientes.append(novo_cliente)
            continue
        case '2': # LISTAR
            i = 0
            for cliente in clientes:
                i = i + 1
                print(f'Cliente {i}  ' + '+'*20)
                for chave in dados:
                    print (f'{chave} : {cliente[chave]}')
                print('-'*30)
                continue
        case '3': # ALTERAR
            for chave in dados:
                novo_cliente[chave] = input(f'Digite o(a) {chave} do cliente: ')
            clientes.append(novo_cliente)
            continue
        case '4': # EXCLUIR
            for chave in dados:
                novo_cliente[chave] = input(f'Digite o(a) {chave} do cliente: ')
            clientes.append(novo_cliente)
            continue
        case '5': # PESQUISAR
            pesquisar = input('Qual o nome do cliente a ser pesquisado? ')
            i = 0
            x = 0
            for cliente in clientes:
                if cliente['Nome'] == pesquisar:
                    x = x + 1
                    enc = i
                    continue
                else:
                    i = i + 1
            if x == 0:
                print('Nenhum cliente encontrado')
            else :
                print(f'Indice {enc}: {clientes[enc]['Nome']}')
                continue
        case '6': # PESQUISAR
            pesquisar = input('Qual o nome do cliente a ser pesquisado? ')
            encontrados = [cliente for cliente in clientes if cliente.get('Nome') == pesquisar]
            if encontrados:
                for i, cliente in enumerate(encontrados, start=1):
                    print(f'Cliente {i}  ' + '+'*20)
                    for chave in dados:
                        print(f'{chave} : {cliente.get(chave, "Não informado")}')
                    print('-'*30)
            else:
                print('Nenhum cliente encontrado.')        
            
            
            
            
            '''
            for chave in dados:
                novo_cliente[chave] = input(f'Digite o(a) {chave} do cliente: ')
            clientes.append(novo_cliente)
            continue
            '''
        case _:
            break
            
    # for chave in dados:
    #    