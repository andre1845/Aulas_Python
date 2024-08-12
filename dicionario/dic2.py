
print('CADASTRO DE CLIENTES')

lista_usuarios = []
i=0
while True:

    usuario = {
                "nome": input("Nome: "),
                "idade": input("Idade: "),
                "cpf": input("CPF: "),
                }
    lista_usuarios.append(usuario)
    
    continuar = input('Continuar ? s/n : ')
    if continuar == 'n':
        for i in range(len(lista_usuarios)):
                print(lista_usuarios[i])
                print(lista_usuarios[i]['nome'])
                print(lista_usuarios[i]['idade'])
                print(lista_usuarios[i]['cpf'])                
        break
    else :
        i = i +1
        continue

    