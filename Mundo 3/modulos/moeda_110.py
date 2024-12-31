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



def resumo(preco, mais=0, menos=0):
    print('-' * 60)
    print('RESUMO'.center(60))
    print('-' * 60)
    print(f'O dobro de {moeda(preco)} é {dobro(preco, format_moeda=True)} e a metade é {metade(preco, format_moeda=True)}!')
    print(f'O valor com um desconto de 15% é { diminuir(preco, menos, True) }')
    print(f'O valor com um aumento de 30% é { aumentar(preco, mais, True) }')