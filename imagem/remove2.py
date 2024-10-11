from rembg import remove
from PIL import Image
import os

while True:
    try:
        # Diretório atual onde o script está rodando
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        
        imagem = input("Imagem para remover fundo (ou aperte Enter para sair): ")
        
        # Caminho absoluto para a imagem
        imagem2 = os.path.join(diretorio_atual, imagem)
        
        if imagem:
            nova_img = os.path.join(diretorio_atual, f"nova_{os.path.basename(imagem)}.png")
            
            # Abrir a imagem original
            original = Image.open(imagem2)
            
            # Remover o fundo
            img_sem_fundo = remove(original)
            
            # Salvar a nova imagem sem fundo
            img_sem_fundo.save(nova_img)
            print(f"Imagem sem fundo salva como {nova_img}")
        
        else:
            print("Encerrando o programa.")
            break
    
    except Exception as e:
        print(f"Não foi possível remover o fundo. Erro: {e}")