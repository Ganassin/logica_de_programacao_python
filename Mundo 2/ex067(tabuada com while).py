# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('-='*35, 'TABOADA', '-='*35)

while True:
    taboada = int(input('Quer saber a taboada de qual número? '))
    limite = int(input('Quer fazer as multiplicações até qual número? '))

    print('-=' * 23)
    for c in range(0, limite + 1):
        print(f'{taboada} x {c} = {c * taboada}')
    print('-=' * 23)

    resp = str(input('\nQuer continuar? (S/N) '))
    if resp in 'Nn':
        break

print('-='*20,' Programa de tebuada encerrado! ', '-='*20)