class Endereco:
    def __init__(self, cep, uf, cidade, bairro):
        #metodo construtor
        self.__cep = cep
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro

    #métodos de acesso
    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def uf(self):
        return self.__uf
    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    #métodos de ação
    def obter_endereco(self):
        return f'{self.__bairro}, cidade de {self.__cidade}, {self.__uf}. CEP: {self.__cep}'

class Telefone:
    def __init__(self, pessoal, residencial, comercial, emergencia):
        self.__pessoal = pessoal
        self.__residencial = residencial
        self.__comercial = comercial
        self.__emergencia = emergencia

    @property
    def pessoal(self):
        return self.__pessoal

    @pessoal.setter
    def pessoal(self, pessoal):
        self.__pessoal = pessoal

    @property
    def residencial(self):
        return self.__residencial

    @residencial.setter
    def residencial(self, residencial):
        self.__residencial = residencial

    @property
    def comercial(self):
        return self.__comercial

    @comercial.setter
    def comercial(self, comercial):
        self.__comercial = comercial

    @property
    def emergencia(self):
        return self.__emergencia

    @emergencia.setter
    def emergencia(self, emergencia):
        self.__emergencia = emergencia

    def obter_contatos(self):
        return f'Pessoal: {self.__pessoal}, Residencial: {self.__residencial}, Comercial: {self.__comercial}, Emergencial: {self.__emergencia}'


class Pessoa:
    #metodo construtor
    def __init__(self, nome, idade, endereco, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco #aqui ocorre a composição
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    #metodos de ação
    def obter_info_pessoal(self):
        return f'{self.__nome}, {self.__idade} anos, mora em {self.__endereco.obter_endereco()}\nContatos: {self.__telefone.obter_contatos()}'
    




