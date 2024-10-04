def mostrar_menu():
    print('1 - Equacao do 1º grau')
    print('2 - Equacao do 2º grau')
    print('3 - Sair')
    
calc_grau_1 = lambda a,b: -b/a
    
def calc_grau_2(a, b, c):
    delta = float((b**2)-(4*a*c))
    if delta < 0:
        return f'A equação não tem raízes reais.'
        
    elif delta == 0:
        return f'O valor de x é {(-b)/(2*a)}'
    else:
        x1 = ((-b)+(delta**(1/2)))/(2*a)
        x2 = ((-b)-(delta**(1/2)))/(2*a)
        return f'Valor de x1 = {x1}', f' Valor de x2 = {x2}'