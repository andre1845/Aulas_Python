import os
from manipulador import *
from pessoas import *

if __name__=="__main__":
    
    p = Pessoa(0,'','','','')
    m = Manipulador()
    
    while True:
    
        print("1 - Criar novo arquivo JSON")
        print("2 - Ler arquivo JSON")
        print("3 - Gravar arquivo JSON")
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
                    usuario['Codigo'] = len(usuarios)
                    
                    # Coleta as informações do novo usuário
                    for campo in campos:
                        usuario[campo.capitalize()] = input(f"Informe {campo.capitalize()}: ")
                    
                   
                    
                    # Adiciona o novo usuário à lista
                    usuarios.append(usuario)
                    
                    # Salva os dados atualizados no arquivo
                    print(m.salvar_dados(usuarios, ler_arquivo))
                
                except Exception as e:
                    print(f"Não foi possível gravar os dados. Erro: {e}")
                finally:
                    continue
                
            case _:
                print("Opção invalida")
                continue