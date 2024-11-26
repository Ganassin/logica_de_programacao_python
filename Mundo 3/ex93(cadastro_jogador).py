# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {
    'Nome': str(input('Qual o nome do jogador? ')),
    'Qnt_partidas': int(input('Quantas partidas ele jogou? '))
}

gols = list()
for qnt in range(jogador['Qnt_partidas']):
    gols.append(int(input(f'Quantos gols ele marcou na partida {qnt+1}? ')))

jogador['Gols'] = gols
jogador['Tot_gols'] = sum(gols)

print(30*'=')
print(jogador)

print(30*'=')
print(f'O jogador {jogador["Nome"]} jogou {jogador["Qnt_partidas"]} partidas e marcou {jogador["Tot_gols"]} gols!')
for partida, gols in enumerate(jogador['Gols']):
    print(f'Gols na partida {partida+1}: {gols}')


