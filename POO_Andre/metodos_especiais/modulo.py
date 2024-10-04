class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        
    def __str__(self):
        return f"Alô, meu nome é {self.nome}, tenho {self.idade} e email {self.email}."
    
    def __repr__(self):
        return f"Pessoa({self.nome}, {self.idade}, {self.email})"
    
    def __len__(self, nome):
        return self.nome
    
    def __del__(self):
        print(f'O objeto {self.nome} foi eliminado.')