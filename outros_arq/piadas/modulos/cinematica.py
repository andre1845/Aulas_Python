def menu():
    print('1 - Energia potencial')
    print('2 - Energia cinética')
    print('3 - Planejar viagem')
    print('5 - Sair')
    
def calcular_ep(m, h):
    ep = m*9.8*h
    return ep

def calcular_ec(m, v):
    ec = m*(v**2)/2
    return ec
    
def consumo(dist, cons_combust):
    consumo = dist / cons_combust
    return consumo

def tempo_viagem(dist, vel):
    tempo = dist / vel
    return tempo

def custo_viagem(val_comb, total_litros):
    custo = val_comb * total_litros
    return custo
    
    
