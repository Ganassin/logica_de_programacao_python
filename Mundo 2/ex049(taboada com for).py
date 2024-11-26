# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

print('-='*35, 'TABOADA', '-='*35)

taboada = int(input('Quer saber a taboada de qual número? '))
limite = int(input('Quer fazer as multiplicações até qual número? '))

for c in range(0, limite+1):
    print(f'{taboada} x {c} = {c * taboada}')