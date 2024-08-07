frutas = ['Maracuja', "maça", "Laranja", "Banana", "uva", "Abacaxi"]

while True:

    for i in range(len(frutas)):
        print(f'{i}) {frutas[i]}')

        
    retirar = int(input('Qual item vai retirar? '))
        
    retirado = frutas.pop(retirar)
        
    print (retirado)
        
    for i in range(len(frutas)):
        print(f'{i}) {frutas[i]}')
    
    continuar = input("Continuar? ")
    if continuar != "n":
        continue
    else:
        break