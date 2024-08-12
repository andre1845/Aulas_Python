import os
os.system('cls')
usuario = {
    'nome':'Andre Andrino',
    'idade':'52',
    'profissão':'desenvolvedor'
}

cliente = [
    {
    'nome':'Cliente 1',
    'idade':'23',
    'profissão':'vendedor'
    }
]

print(usuario['nome'])
print(usuario['idade'])
print(usuario['profissão'])

print(cliente[0]['nome'])
print(cliente[0]['idade'])
print(cliente[0]['profissão'])

print(usuario.get('nome'))
print(usuario.get('idade'))
print(usuario.get('profissão'))
print(usuario.get('email'))

usuario['email'] = 'rolha@mail.com'
print(usuario.get('email'))

print(len(usuario))
chaves = usuario.keys()
valores = usuario.values()
items = usuario.items()
print(chaves)
print(valores)
print(items)

for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')
    
usuario['email'] = input('Informe o novo email: ')