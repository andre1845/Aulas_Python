import os
lista_notas = []
i = 1
print ('Digite as notas abaixo. ')
while True:
    os.system('cls')
    nota_input = input(f'Digite a {i}ª nota (Deixe em branco para encerrar)')
    
    i = i+1
    if nota_input != "":
        nota = float(nota_input)
        lista_notas.append(nota)
        continue
    else:
        
        qtde = len(lista_notas)
        soma = sum(lista_notas)
        media = soma/qtde
        print(f'\nA média das {qtde} notas é {media:,.2f}')
        
    continuar = input('Deseja calcular outra média? (s/n) ')
    if continuar != "n":
        i=1
        lista_notas = []
        continue
    else:
        break
