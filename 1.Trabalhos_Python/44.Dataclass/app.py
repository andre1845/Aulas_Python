from modulo import *

if __name__ == "__main__":
    usuario = Pessoa('Bruna', 39, 1.72)
    
    print(f"Nome: {usuario.nome}")
    print(f"idade: {usuario.idade}")
    print(f"altura: {usuario.altura}")
    
    usuario.nome = "Andre"
    print(f"Nome: {usuario.nome}")