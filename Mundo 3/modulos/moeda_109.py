def moeda(valor=0, moeda = 'R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')

def aumentar(valor=0, percent=0, format_moeda=False, sifra = 'R$'):
    percent = percent/100
    if format_moeda == True:
        return moeda((valor * (1 + percent)), moeda = sifra)
    else:
        return (valor * (1 + percent))

def diminuir(valor=0, percent=0, format_moeda=False, sifra = 'R$'):
    percent = percent/100
    if format_moeda == True:
        return moeda((valor * (1 - percent)), moeda = sifra)
    else: 
        return (valor * (1 - percent))

def dobro(valor=0, format_moeda=False, sifra = 'R$'):
    if format_moeda == True:
        return moeda(valor*2, moeda = sifra)
    else:
        return valor*2

def metade(valor=0, format_moeda=False, sifra = 'R$' ):
    if format_moeda == True: 
        return moeda((valor/2), moeda = sifra)
    else:
        return (valor/2) 





