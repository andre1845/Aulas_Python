

# NOTE : classe carro

class Carro:
    # Atributos
    fabricante = 'Volkswagen'
    modelo = 'Gol'
    ano = '2000'
    cor = 'preto'
    placa ='ABC-1234'
    
    # metodos
    
    def ligar(self, ignicao):
        if (ignicao):
            return f'{self.modelo} está ligado'
        else :
            return f'{self.modelo} está desligado'
        
# NOTE : programa principal
 
if __name__ == '__main__':
# instanciar a classe carro (criar objeto)

    meu_carro = Carro()

#exibir atributos do objeto

    print(f'Fabricante: {meu_carro.fabricante}.')
    print(f'Modelo: {meu_carro.modelo}.')
    print(f'Ano: {meu_carro.ano}.')
    print(f'Cor: {meu_carro.cor}.')
    print(f'Placa: {meu_carro.placa}.')
    
    print(meu_carro.ligar(False))