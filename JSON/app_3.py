import os
from manipulador import *
from pessoas import *

if __name__=="__main__":
    
    p = Pessoa(0,'','','','')
    m = Manipulador()
    
    while True:
        print("1 - Criar novo arquivo JSON")
        print("2 - Ler arquivo JSON")
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
                try:
                    usuario = {}
                    campos = ('nome','cpf', 'email','profissao')
                    print(f"Arquivo aberto: {ler_arquivo}.json\n ")
                    for campo in campos:
                        usuario[campo] = input(f"Informe {campo.capitalize()}: ")
                    usuario[codigo] = len(usuarios)
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, ler_arquivo))
                except Exception as e:
                    print('Não foi possivel gravar os dados.')
                finally:
                    continue
                
            case _:
                print("Opção invalida")
                continue