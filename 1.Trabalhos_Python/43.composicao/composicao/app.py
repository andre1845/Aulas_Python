from modulo import *

if __name__ == '__main__':
    #instanciando os objetos
    endereco_pessoal = Endereco('','','','')
    telefones = Telefone('','','','')
    usuario = Pessoa('',0,'','')

    #entrada de dados
    usuario.nome = input('Informe o nome do usuário: ')
    usuario.idade = input('Informe a idade do usuário: ')
    

    #composicao de dados do endereco
    usuario.endereco = endereco_pessoal

    #composicao de dados do telefone
    usuario.telefone = telefones

    #entrada de dados do endereco
    usuario.endereco.cep = input('Informe o CEP: ')
    usuario.endereco.uf = input('Informe a UF: ')
    usuario.endereco.cidade = input('Informe a cidade: ')
    usuario.endereco.bairro = input('Informe o bairro: ')
    usuario.telefone.pessoal = input('Informe o telefone pessoal: ')
    usuario.telefone.residencial = input('Informe o telefone residencial: ')
    usuario.telefone.comercial = input('Informe o telefone comercial: ')
    usuario.telefone.emergencia = input('Informe o telefone emergencia: ')
    
    #saída de dados
    print(usuario.obter_info_pessoal())
