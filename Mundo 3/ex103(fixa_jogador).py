# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha (nome='', gols=0):
    print('=-'*10)
    
    if not nome:
        print(str.center(f'Nome: <desconhecido>', 20))
    else:
        print(str.center(f'Nome: {nome}', 20))
    
    if gols == 0:
        print(str.center(f'Gols: <não registrado>', 20)) 
    else:    
        print(str.center(f'Gols: {gols}', 20))
    
    print('=-'*10)

ficha(gols=10)