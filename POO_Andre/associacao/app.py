
from modulo import *

if __name__ == "__main__":
    
    aluno1 = Aluno('','','')
    aluno2 = Aluno('','','')
    aluno3 = Aluno('','','')
    curso1 = Curso('',0,'')
    curso2 = Curso('',0,'')
    
    aluno1.nome = input('Nome? ')
    aluno1.matricula = input('Matricula? ')
    aluno1.cpf = input('CPF ? ')
    
    aluno2.nome = input('Nome? ')
    aluno2.matricula = input('Matricula? ')
    aluno2.cpf = input('CPF ? ')
    
    aluno3.nome = input('Nome? ')
    aluno3.matricula = input('Matricula? ')
    aluno3.cpf = input('CPF ? ')
    
    
    curso1.nome = input('Curso? ')
    curso1.duracao = input('Duração? ')
    curso1.turno = input('Turno ? ')
    
    curso2.nome = input('Curso? ')
    curso2.duracao = input('Duração? ')
    curso2.turno = input('Turno ? ')
    
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso2)
    aluno3.inscrever_curso(curso2)
    
    print(f'Aluno {aluno1.nome} de matr {aluno1.matricula} está inscrito no curso {aluno1.listar_cursos()}.')
    print(f'Aluno {aluno2.nome} de matr {aluno2.matricula} está inscrito no curso {aluno2.listar_cursos()}.')
    print(f'No curso {curso1.nome} estao matriculados os alunos {curso1.listar_alunos()}')
    print(f'No curso {curso2.nome} estao matriculados os alunos {curso2.listar_alunos()}')
    
    
    print(aluno1.nome)
    print(aluno1.matricula)
    print(aluno1.cpf)
    
    print(aluno2.nome)
    print(aluno2.matricula)
    print(aluno2.cpf)
    
    print(curso1.nome)
    print(curso1.duracao)
    print(curso1.turno)