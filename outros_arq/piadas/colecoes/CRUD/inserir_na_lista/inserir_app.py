cobras = ['sucuri', 'piton', 'mamba negra', 'naja']

cobras.append('cascavel')
cobras.append('anaconda')

while True:
    cobras.sort()
    i=0
    for cobra in cobras:
        i+=1
        print(f'{i}. {cobra}')
    print('x'*30)    

    nova_cobra = input("Digite uma nova cobra : ")
    cobras.append(nova_cobra)

    i=0
    for cobra in cobras:
        i+=1
        print(f'{i}. {cobra}')
    print('-'*50)  
    
    '''   
    cobras.sort(reverse=True)
    for cobra in cobras:
        print(cobra)
    '''
    continuar = input("Continuar s/n? ")
    if(continuar.lower() != 'n'):
        continue
    else:
        break