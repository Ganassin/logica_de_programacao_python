from random import randint
# Gera e Armazena 5 números aleatórios em uma TUPLA
numeros = (randint(0,100), randint(0,100),
           randint(0,100), randint(0,100),
           randint(0,100))
print(numeros, '\n')

# Verifica toda a TUPLA para encontrar o maior e o menor
maior = menor = cont = 0
for x in numeros:
    if x > maior:
        maior = x

    if cont == 0:
        menor = x
    else:
        if x < menor:
            menor = x
    cont += 1

print(f' O menor número da TUPLA é {menor}')
print(f' O maior número da TUPLA é {maior}')

print('OU'.center(30, '.'))
# as duas linhas a baixo fazem a mesma coisa que o códio da linha 7 à 20
print(f' O menor número da TUPLA é {min(numeros)}')
print(f' O maior número da TUPLA é {max(numeros)}')
