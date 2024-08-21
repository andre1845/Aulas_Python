import secrets

while True:
    confirma = input('Deseja gerar uma senha (s/n)? ').lower()

    if confirma == 's':
        print(secrets.token_urlsafe(16))#secrets a biblioteca .token_urlsafe() a função dessa biblioteca 16 é o numero de caracteres
        continue
    else:
        print('Progama encerrado')
        break