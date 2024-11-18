from random import randint

aleatorio = randint(0, 5)
num = int(input('Escolha um número inteiro de 1 a 5: '))

if num == aleatorio:
    print('Parabéns, você acertou!!!')
else:
    print('Não foi dessa vez!')

