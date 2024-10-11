import os

def buscar_arquivo(nome_arquivo, diretorio):
    """Busca recursivamente por um arquivo no diretório especificado."""
    for raiz, dirs, arquivos in os.walk(diretorio):
        if nome_arquivo in arquivos:
            return os.path.join(raiz, nome_arquivo)
    return None

def main():
    # Diretório inicial para a busca (pode ser a raiz do sistema, como C:\ ou /)
    diretorio_inicial = os.path.expanduser("~")  # Diretório home do usuário

    # Solicitar ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo (incluindo a extensão): ")

    # Buscar o arquivo
    caminho = buscar_arquivo(nome_arquivo, diretorio_inicial)

    # Imprimir o resultado
    if caminho:
        print("Arquivo encontrado:", caminho)
    else:
        print("Arquivo não encontrado.")

if __name__ == "__main__":
    main()
