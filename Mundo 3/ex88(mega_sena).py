import random, time

dados = []
jogos = []

print('-'*32)
print('Sorteador de jogos da Mega Sena!')
print('-'*32)

qnt_jogos = int(input('Quantos jogos deseja sortear? '))

for a in range(0, qnt_jogos):
    for n in range(0, 6):
        numero = random.randint(1, 61)
        while numero in dados:
            numero = random.randint(1, 61)
        dados.append(numero)

    jogos.append(sorted(dados[:]))
    dados.clear()
    time.sleep(0.7)
    print(f'Jogo {a+1}: {jogos[a]}')

