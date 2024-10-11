from rembg import remove
from PIL import Image
import os

while True:
    try:
         # Diretório atual onde o script está rodando
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        
        imagem = input("Imagem para remover fundo: ")
            
            # Caminho absoluto para o arquivo JSON
        imagem2 = os.path.join(diretorio_atual, f"{imagem}")
        if imagem:
            nova_img = f"nova_{imagem2}.png"
            original = Image.open(imagem2)
            img_sem_fundo = remove(original)
            img_sem_fundo.save(nova_img)
            continue
        else:
            ...
    except Exception as e:
        print(f"Não foi possível remover o fundo {e}")
    finally:
        break