import os
from manipulador import *
from pessoas import *

def gerar_proximo_codigo(usuarios):
    if usuarios:
        return max([usuario['codigo'] for usuario in usuarios]) + 1
    return 1  # Caso a lista esteja vazia, retorna 1 como primeiro código

def encontrar_usuario_por_codigo(usuarios, codigo):
    for usuario in usuarios:
        if usuario['codigo'] == codigo:
            return usuario
    return None

if __name__ == "__main__":
    
    p = Pessoa(0, '', '', '', '')
    m = Manipulador()
    
    ler_arquivo = ''  # Inicializa para verificar se um arquivo foi carregado
    
    while True:
        print("1 - Criar novo arquivo JSON")
        print("2 - Ler arquivo JSON")
        print("3 - Gravar no arquivo JSON")
        print("4 - Alterar no arquivo JSON")
        print("5 - Excluir no arquivo")
        print("0 - Sair")
        
        opcao = input("Digite a opção: ")
        os.system('cls')
        
        match opcao:
            case '0':
                print('Programa finalizado')
                break
            case '1':
                novo_arquivo = input("Nome do arquivo a ser criado: ")
                print(m.criar_arquivo(novo_arquivo))
                ler_arquivo = novo_arquivo  # Definimos o novo arquivo como o atual
                continue
            case '2':
                ler_arquivo = input("Qual arquivo deseja abrir? ")
                try:
                    os.system('cls')
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    print(f"Arquivo aberto: {ler_arquivo}.json\n")
                    for usuario in usuarios:
                        for campo, valor in usuario.items():
                            print(f"{campo.capitalize()}: {valor}")
                        print(f"\n{'-'*30}\n")
                except Exception as e:
                    print(f"Não foi possível abrir o arquivo. Erro: {e}")
                finally:
                    continue
            case '3':
                if not ler_arquivo:
                    print("Nenhum arquivo foi carregado ou criado. Abra ou crie um arquivo primeiro.")
                    continue
                
                try:
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    print(f"Gravando no arquivo: {ler_arquivo}.json\n")
                    
                    # Gerar o próximo código e capturar os dados do novo usuário
                    p.codigo = gerar_proximo_codigo(usuarios)
                    p.nome = input("Nome: ")
                    p.cpf = input("CPF: ")
                    p.email = input("Email: ")
                    p.profissao = input("Profissão: ")
                    
                    # Cria o dicionário do novo usuário
                    usuario = dict(codigo=p.codigo, nome=p.nome, cpf=p.cpf, email=p.email, profissao=p.profissao)
                    usuarios.append(usuario)
                    
                    print(m.salvar_dados(usuarios, ler_arquivo))
                    print(f"Usuário {p.nome} gravado com sucesso!")
                
                except Exception as e:
                    print(f"Não foi possível gravar os dados. Erro: {e}")
                finally:
                    continue
            case '4':
                if not ler_arquivo:
                    print("Nenhum arquivo foi carregado ou criado. Abra ou crie um arquivo primeiro.")
                    continue
                
                try:
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    codigo = int(input("Informe o código do usuário que deseja alterar: "))
                    usuario = encontrar_usuario_por_codigo(usuarios, codigo)
                    
                    if usuario:
                        for campo, valor in usuario.items():
                            novo_dado = input(f"{campo.capitalize()} atual: {valor}. Novo valor (ou ENTER para manter): ")
                            if novo_dado:
                                usuario[campo] = novo_dado
                        print(m.salvar_dados(usuarios, ler_arquivo))
                        print("Usuário alterado com sucesso!")
                    else:
                        print(f"Usuário com código {codigo} não encontrado.")
                    
                except Exception as e:
                    print(f"Não foi possível alterar os dados. Erro: {e}")
                finally:
                    continue
            case '5':
                if not ler_arquivo:
                    print("Nenhum arquivo foi carregado ou criado. Abra ou crie um arquivo primeiro.")
                    continue
                
                try:
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    codigo = int(input("Informe o código do usuário que deseja EXCLUIR: "))
                    usuario = encontrar_usuario_por_codigo(usuarios, codigo)

                    if usuario:
                        nome_deletado = usuario['nome']
                        confirmacao = input(f"Apagar {nome_deletado} (s/n)? ").lower()
                        if confirmacao == 's':
                            usuarios.remove(usuario)
                            print(m.salvar_dados(usuarios, ler_arquivo))
                            print(f"Usuário {nome_deletado} excluído com sucesso!")
                        else:
                            print("Exclusão CANCELADA!")
                    else:
                        print(f"Usuário com código {codigo} não encontrado.")
                    
                except Exception as e:
                    print(f"Não foi possível excluir os dados. Erro: {e}")
                finally:
                    continue
            case _:
                print("Opção inválida")
                continue
