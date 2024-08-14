clientes = [
    {'Nome': 'Fulano', 'Idade': 20, 'Profissão': 'Programador'},
    {'Nome': 'Alberto', 'Idade': 32, 'Profissão': 'Desenvolvedor'},
    {'Nome': 'Mario', 'Idade': 20, 'Profissão': 'Eletricista'},
    {'Nome': 'Roberta', 'Idade': 41, 'Profissão': 'Policial'}
]

# Acessar diretamente pelo índice
print(clientes[0]['Nome'])  # Output: Fulano

# Iterar pela lista
for cliente in clientes:
    print(cliente['Nome'], cliente['Idade'])

# Usar enumerate
for indice, cliente in enumerate(clientes):
    print(f'Cliente {indice}: {cliente["Nome"]}, {cliente["Idade"]}')

# Compreensão de lista
nomes = [cliente['Nome'] for cliente in clientes]
print(nomes)  # Output: ['Fulano', 'Alberto', 'Mario', 'Roberta']

# Usar next para encontrar um único item
cliente = next((cliente for cliente in clientes if cliente['Nome'] == 'Alberto'), None)
print(cliente)  # Output: {'Nome': 'Alberto', 'Idade': 32, 'Profissão': 'Desenvolvedor'}

# Usar filter para encontrar vários itens
clientes_maiores_25 = list(filter(lambda cliente: cliente['Idade'] > 25, clientes))
print(clientes_maiores_25)

# Acessar valores com get
for cliente in clientes:
    print(cliente.get('Nome', 'Nome não informado'))
    print(cliente.get('Idade', 'Idade não informada'))
