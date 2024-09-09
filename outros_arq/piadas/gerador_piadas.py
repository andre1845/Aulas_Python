#importa bibliotecas
import pyjokes
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto', target='pt')#source='auto' identifica em qual idioma esta / target='pt' pra qual é pra traduzir

while True:
    piada = pyjokes.get_joke() #gera uma piada get_joke puxa uma piada
    piada_traduzida = tradutor.translate(piada) 
    print(piada_traduzida)

    repetir = input('Deseja gerar outra piada (s/n)? ').lower()
    if repetir == 's':
        continue
    else:
        break
    