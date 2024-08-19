# Comando WHILE com if else -> continue / break --> loop infinito


while True:
    nome = input('Nome:')
    idade = int(input('Idade:'))

    if idade >= 18:
        print(f'{nome} é maior')
    else:
        print(f'{nome} é menor')
    
    continuar = input('Continuar (s/n)? ')

    if continuar == 's':
        continue
    else:
        break