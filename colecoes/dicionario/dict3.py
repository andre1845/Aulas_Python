usuarios = [
    {'Nome':  'Fulano',
     'Idade': 20,
     'Profissão': 'Programador',
    },
    {'Nome':  'Alberto',
     'Idade': 32,
     'Profissão': 'Desenvolvedor',
    },
    {'Nome':  'Mario',
     'Idade': 20,
     'Profissão': 'Eletricista',
    },
    {'Nome':  'Roberta',
     'Idade': 41,
     'Profissão': 'Policial',
    }   
]

chaves = ["Nome", "Idade", "Profissão"]

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
