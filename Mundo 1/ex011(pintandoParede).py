largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura

print(f'\nA parede a ser pintada tem dimensão de {largura}m x {altura}m, logo sua área é {area}m²\n'
      f'Para pintar você precisará de {0.5*area}l de tinta!')