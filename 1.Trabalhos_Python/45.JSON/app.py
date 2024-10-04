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

if __name__=="__main__":
    
    p = Pessoa(0,'','','','')
    m = Manipulador()
    
    while True:
    
        print("1 - Criar novo arquivo JSON")
        print("2 - Ler arquivo JSON")
        print("3 - Gravar no arquivo JSON")
        print("4 - Alterar no arquivo JSON")
        print("5 - Excluir no arquivo")
        print("0 - Sair")
        
        opcao = input("Digite a opcao: ")
        os.system('cls')
        
        match opcao:
            case '0':
                print('Programa finalizado')
                break
            case '1':
                novo_arquivo = input("Nome do arquivo a ser criado: ")
                print(m.criar_arquivo(novo_arquivo))
                continue
            case '2':
                ler_arquivo = input("Qual arquivo deseja abrir? ")
                try:
                    os.system('cls')
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    print(f"Arquivo aberto: {ler_arquivo}.json\n ")
                    for i in range(len(usuarios)):
                        for campo, valor in usuarios[i].items():
                            print(f"{campo.capitalize()}: {valor}")
                        print(f"\n{'-'*30}\n")
                except Exception as e:
                    print('Não foi possivel abrir o arquivo.')
                finally:
                    continue
            case '3':
                if not ler_arquivo:
                    print("Nenhum arquivo foi carregado ou criado. Abra ou crie um arquivo primeiro.")
                    continue
                
                try:
                    usuario = {}
                    campos = ('nome', 'cpf', 'email', 'profissao')
                    
                    # Garante que o arquivo foi lido
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    
                    print(f"Gravando no arquivo: {ler_arquivo}.json\n ")
                     # Define o código do novo usuário como o próximo número na lista
                    '''
                    usuario['Codigo'] = len(usuarios)
                    
                    # Coleta as informações do novo usuário
                    for campo in campos:
                        usuario[campo.capitalize()] = input(f"Informe {campo.capitalize()}: ")
                    
                    # Adiciona o novo usuário à lista
                    usuarios.append(usuario)
                    
                    # Salva os dados atualizados no arquivo
                    print(m.salvar_dados(usuarios, ler_arquivo))
                    '''
                    print(f"Arquivo aberto: {ler_arquivo}.json.\n")
                    p.codigo = len(usuarios)
                    p.nome = input("Nome: ")
                    p.cpf = input("cpf: ")
                    p.email = input("Email: ")
                    p.profissao = input("Profissao: ")
                    usuario = dict(codigo=p.codigo, nome=p.nome, cpf=p.cpf, email=p.email, profissao=p.profissao)
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, ler_arquivo))
                
                except Exception as e:
                    print(f"Não foi possível gravar os dados. Erro: {e}")
                finally:
                    continue
            case '4':
                try:
                    if not ler_arquivo:
                        print("Nenhum arquivo foi carregado ou criado. Abra ou crie um arquivo primeiro.")
                    # Garante que o arquivo foi lido
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    
                    print(f"Gravando no arquivo: {ler_arquivo}.json\n ")
                     # Define o código do novo usuário como o próximo número na lista
                    codigo = int(input("Informe o codigo do usuario que deeja alterar: "))
                    if usuarios[codigo]:
                        for campo in usuarios[codigo]:
                            novo_dado = input(f"{campo} atual: {usuarios[codigo].get(campo)}. Novo valor (ou ENTER para manter): ")
                            if novo_dado:
                                usuarios[codigo][campo] = novo_dado
                        print(m.salvar_dados(usuarios, ler_arquivo))
                        print("Usuário alterado com sucesso!")
                    else:
                        print(f"Usuário com código {codigo} não encontrado.")
                    
                    print(m.salvar_dados(usuarios, ler_arquivo))
                             
                except:
                     print(f"Não foi possível alterar os dados. Erro: {e}")
                finally:
                    continue
            case '5':
                try:
                    if not ler_arquivo:
                        print("Nenhum arquivo foi carregado ou criado. Abra ou crie um arquivo primeiro.")
                    # Garante que o arquivo foi lido
                    usuarios = m.abrir_arquivo(ler_arquivo)
                    
                    print(f"Gravando no arquivo: {ler_arquivo}.json\n ")
                     # Define o código do novo usuário como o próximo número na lista
                    codigo = int(input("Informe o codigo do usuario que deseja EXCLUIR: "))

                    if usuarios[codigo]:
                        nome_deletado = usuarios[codigo]['nome']
                        confirmacao = input(f"Apagar {nome_deletado} (s/n)? ").lower()
                        if confirmacao == 's':
                            del(usuarios[codigo])
                            print(m.salvar_dados(usuarios, ler_arquivo))
                            print(f"Usuário {nome_deletado} excluído com sucesso!")
                        else:
                            print("Exclusão CANCELADA!")
                    else:
                        print(f"Usuário com código {codigo} não encontrado.")
                    
                except:
                     print(f"Não foi possível excluir os dados. Erro: {e}")
                finally:
                    continue
                            
            case _:
                print("Opção invalida")
                continue