from modulo_heranca_mult import *
   

if __name__ == '__main__':
    #instanciando objeto da subclasse
    h = Filha('','','','',0.0,0.0,'')

    #entrada de dados
    h.nome = input('Informe o nome: ')
    h.email = input('Informe o email: ')
    h.profissao = input('Informe a profissao: ')
    h.olhos = input('Informe a cor dos olhos: ')
    h.peso = float(input('Informe o peso: ').replace(',','.'))
    h.altura = float(input('Informe a altura: ').replace(',','.'))
    h.cor_cabelo = input('Informe a cor do cabelo: ')

    print('\n')
    print(f'{'-'*10} Dados {'-'*10}')
    h.exibir_cartao_visita()
    h.exibir_fisico()