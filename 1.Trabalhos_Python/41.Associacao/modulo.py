class Aluno:
    def __init__(self,nome, matricula, cpf):
        self.__nome = nome
        self.__matricula = matricula
        self.__cpf = cpf
        self.cursos_inscritos = []

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _matricula(self):
        return self.__matricula

    @_matricula.setter
    def _matricula(self, value):
        self.__matricula = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)
            
    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome)
        return lista
    
    
class Curso:
    def __init__(self, nome,duracao,turno):
        self.__nome = nome
        self.__duracao = duracao
        self.__turno = turno
        self.alunos_inscritos = []
        
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao
        
    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self, turno):
        self.__turno = turno
        
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            aluno.inscrever_curso(self)
    
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)
        return lista