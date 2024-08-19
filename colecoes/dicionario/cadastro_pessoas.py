
print('CADASTRO DE CLIENTES')

lista_usuarios = []

usuario = {
            "nome": input("Nome: "),
            "idade": input("Idade: "),
            "cpf": input("CPF: "),
            "rg": input("RG: "),
            "data_nasc": input("Data de Nascimento (DD/MM/AAAA): "),
            "sexo": input("Sexo: "),
            "signo": input("Signo: "),
            "mae": input("Nome da Mãe: "),
            "pai": input("Nome do Pai: "),
            "email": input("Email: "),
            "senha": input("Senha: "),
            "cep": input("CEP: "),
            "endereco": input("Endereço: "),
            "numero": input("Número: "),
            "bairro": input("Bairro: "),
            "cidade": input("Cidade: "),
            "estado": input("Estado: "),
            "telefone_fixo": input("Telefone Fixo: "),
            "celular": input("Celular: "),
            "altura": input("Altura: "),
            "peso": input("Peso: "),
            "tipo_sanguineo": input("Tipo Sanguíneo: "),
            "cor": input("Cor Favorita: "),
            }
lista_usuarios.append(usuario)

for chave, valor in usuario.items():
    print(f'{chave} =>........{valor}')
    





