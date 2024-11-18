times = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro',  'Atlético-MG', 'Bragantino',
         'Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco', 	'Criciúma', 'Juventude', 'Corinthians',
         'Fluminense', 	'Vitória', 'Atlético-GO', 'Cuiabá')

print('-='*30)
print("Estatísticas do Brasileirão".center(59 ))
print('-='*30)

print(f'\nOs 5 primeiros são: {times[:5]}')
print('-='*30)
print(f'Os 4 últimos da tabela são: {times[-4:]}')
print('-='*30)
print(f'A tabela em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Flamento está na posição {times.index("Flamengo")+1}\n')

escolha = str(input('Para qual time você torce? ')).lower().capitalize()
while escolha not in times:
    escolha = str(input('Erro! Digite novamente: ')).lower().capitalize()
print(f'Seu time está na posição {times.index(escolha)+1}. Vamos {escolha}!!!')