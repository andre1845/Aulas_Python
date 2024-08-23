
import random

def menu():
    print('1 - Inserir nomes na lista')
    print('2 - Verificar nomes na lista')
    print('3 - Sortear um nome')
    print('4 - Apagar TODOS os nomes da lista')
    print('5 - Remover um nome da lista')
    print('6 - Sair')


def formatar_nome(nome):
    # Remove espaços extras e caracteres não alfabéticos
    nome = nome.strip()
    if not nome:
        return None
    
    nome = ''.join(letra for letra in nome if letra.isalpha() or letra.isspace())  # Remove caracteres especiais
    nome = ' '.join(nome.split())  # Remove espaços extras

    if not nome or not nome.replace(' ', '').isalpha():
        return None  # Retorna None se não restar texto válido
    
    return nome.title()  # Capitaliza o nome


nomes = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case '1':
            print('-'*50)
            while True:
                entrada = input("Digite um nome (ou 'fim' para terminar): ")
                if entrada.lower() == 'fim':
                    break
                
                nome_formatado = formatar_nome(entrada)
                if nome_formatado:
                    nomes.append(nome_formatado)
                else:
                    print("Nome inválido. Tente novamente.")
                    print('-'*50)
                    continue
        case '2':
            print('-'*50)
            if nomes:
                print("Nomes na lista:")
                for nome in nomes:
                    print(f"- {nome}")
                print('-'*50)
                continue
            else:
                print("Nenhum nome na lista.")
                print('-'*50)
                continue
        case '3':            
            sorteado = random.choice(nomes)
            print('*'*50)
            print(f'O nome sorteado foi: {sorteado}.')
            print('*'*50)
            continue
        case '4':
            nomes = []
            print('-'*50)
            print('Lista vazia !')
            print('-'*50)
            continue
        case '5':
            print('-'*50)
            i = 0
            retirar = input('Qual nome deseja remover da lista? ')
            retirar_nome = formatar_nome(retirar)
            
            while retirar_nome in nomes:
                nomes.remove(retirar_nome)
                i += 1
                
            if i != 0:
                print(f'{i} ocorrências de {retirar_nome} foram removidas da lista.')
                print('-'*50)
                continue
            else:
                print(f'O nome {retirar_nome} não foi encontrado na lista.')
                print('-'*50)
                continue    
    
        case '6':
            print('-'*50)
            print("Saindo do programa...")
            break
        case _:
            print('-'*50)
            print("Opção inválida. Tente novamente.")
            print('-'*50)
            continue


    