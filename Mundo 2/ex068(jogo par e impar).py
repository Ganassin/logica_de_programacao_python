# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint

print('-='*30, '\nVamos jogar PAR ou ÍMPAR\n', '-='*30)

num = maquina = vitorias = 0
par_impar = ''
while True:
    # Valida se o usuário escolheu uma opção válida
    par_impar = ' '
    while par_impar not in 'PpIi':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).strip()[0]

    usuario = int(input('\nQuantos dedos você vai jogar?: '))
    maquina = randint(0, 10)

    # ifs para saber se ganhou ou perdeu
    if (usuario+maquina)%2 == 0 and par_impar in 'Pp':
        print(f'\nVocê jogou {usuario} e o computador {maquina}. Total {usuario+maquina} deu PAR!')
        print('---- Você Venceu! ----')
        vitorias += 1
    elif (usuario+maquina)%2 == 0 and par_impar in 'Ii':
        print(f'\nVocê jogou {usuario} e o computador {maquina}. Total {usuario+maquina} deu PAR!')
        print('---- Você Perdeu! ----\n')
        break
    elif (usuario+maquina)%2 != 0 and par_impar in 'Ii':
        print(f'\nVocê jogou {usuario} e o computador {maquina}. Total {usuario+maquina} deu ÍMPAR!')
        print('---- Você Venceu! ----')
        vitorias += 1
    elif (usuario+maquina)%2 != 0 and par_impar in 'Pp':
        print(f'\nVocê jogou {usuario} e o computador {maquina}. Total {usuario+maquina} deu ÍMPAR!')
        print('---- Você Perdeu! ----\n')
        break

    ''''# if para saber se quer continuar o jogo, neste caso, retirar o "break" após o aviso de derrota.
    novo_jogo = str(input('\nQuer jogar novamente? [S/N] ')).strip()[0]
    if novo_jogo in 'Nn':
        break'''

print('-='*30, f'\nGAME OVER! Você ganhou {vitorias} vezes!\n', '-='*30)