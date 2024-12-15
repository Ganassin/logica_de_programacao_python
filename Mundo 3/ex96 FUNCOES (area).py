# Função
def area_terreno (largura, comprimento):
    area = largura * comprimento
    print(f'O terreno de largura {largura} e comprimento {comprimento} tem {area} m² de área')


# Código principal
largura = float(input('Largura do terreno (m): '))
comprimento = float(input('Comprimento do terreno (m): '))

area_terreno(largura, comprimento)