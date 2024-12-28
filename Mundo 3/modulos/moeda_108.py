def aumentar(valor=0, percent=0):
    percent = percent/100
    return (valor * (1 + percent))

def diminuir(valor=0, percent=0):
    percent = percent/100
    return (valor * (1 - percent))

def dobro(valor=0):
    return valor*2


def metade(valor=0):
    return (valor/2) 

def moeda(valor=0, moeda = 'R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')


