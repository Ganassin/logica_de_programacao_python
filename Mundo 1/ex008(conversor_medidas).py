dist = float(input('Uma distância em metros: '))
print(f'Esses {dist}m correspondem a:\n'
      f'{dist/1000} km\n'
      f'{dist/100} hm\n'
      f'{dist/10} dam\n'
      f'{dist*10:.0f} dm\n'
      f'{dist*100:.0f} cm\n'
      f'{dist*1000:.0f} mm\n')
