# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()

while True:
    jogador = {
        'Nome': str(input('\nQual o nome do jogador? ')),
        'Qnt_partidas': int(input('Quantas partidas ele jogou? '))
    }

    gols = list()
    for qnt in range(jogador['Qnt_partidas']):
        gols.append(int(input(f'   Quantos gols ele marcou na partida {qnt+1}? ')))

    jogador['Gols'] = gols
    jogador['Tot_gols'] = sum(gols)

    time.append(jogador.copy())
    jogador.clear()

    while True:
        resposta = str(input('\nDeseja continuar? [S/N]')).strip().upper()
        if resposta in ('S', 'N'):
            break
        else:
            print('\nDigite S ou N!')

    if resposta == 'N':
        break


for x in time:
    print(f'\n{x["Nome"]} marcou {x["Tot_gols"]} em {x["Qnt_partidas"]} partidas jogadas!')
    print(f'Seu aproveitamento foi de {round(x["Tot_gols"]/x["Qnt_partidas"], 2)} gols por partida!\n')

