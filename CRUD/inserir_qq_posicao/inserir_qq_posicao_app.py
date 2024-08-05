nomes = ['Andre', 'Marcia','Roberta']

while True:
    novo_nome = input('digite novo nome ')

    posicao = int(input('Qual a posicao? '))

    nomes.insert(posicao, novo_nome)
    i=0
    for nome in nomes:
        i+=1
        print(f'{i}. {nome.upper()}')
        
    nomes.sort()
    
    continuar = input('Continuar s/n? ')
    if continuar == 's':
        continue
    else:
        break