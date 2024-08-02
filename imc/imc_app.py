import os

while True:
    print(f'{'<'*30} IMC {'>'*30}')
    nome = input('Nome: ')
    peso = input('Peso (em kg) :')
    altura = input('Altura (em metros) :')
    imc = float(float(peso)/(float(altura)*float(altura)))
    print (format(imc, ".2f"))

    if imc < 18.5:
        print(f'{nome}, seu peso está abaixo do normal')
    elif imc >= 18.5 and imc < 25 :
        print(f'{nome}: Peso normal')
    elif imc >= 25 and imc < 30 :
        print(f'{nome}: Pré-Obesidade')
    elif imc >= 30 and imc < 35 :
        print(f'{nome}: Obesidade Grau I')
    elif imc >= 35 and imc < 40 :
        print(f'{nome}: Obesidade Grau II')
    else:
        print(f'{nome}: Obesidade Grau III')
   
    # Valores e Classificação:

    '''
    18.50 – 24.99: Peso Normal
    25.00 – 29.99: Pré-Obesidade
    30.00 – 34.99: Obesidade Grau I
    35.00 – 39.99: Obesidade Grau II
    ≥40.00: Obesidade Grau III
    '''
    print(f'{imc:,.5f}')

    continuar = input('Continuar ?')
    if continuar.lower() == "s":
        os.system('cls')
        continue
    else:
        break
    