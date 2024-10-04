class Pessoa:
    cidade = "Brasilia"
    telefone = "(61)998854545"
    email = "nome@gmail.com"
    
class PessoaFisica(Pessoa):
    nome = "Rolha"
    cpf = "123.456.789-99"
    peso = 90
    altura = 1.50
    
class PessoaJuridica(Pessoa):
    nome_fantasia = "CobraKay"
    cnpj = "333.456.888-99"
    
if __name__ == '__main__':
    
    
    usuario = PessoaFisica()
    empresa = PessoaJuridica()
    
    
print(f'Nome {usuario.nome}')
print(f'cpf {usuario.cpf}')
print(f'email {usuario.email}')
print(' ')

print(f'email {empresa.email}')

