# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

lista = sorted([n1, n2, n3], reverse=True) # Ordena a lista em ordem decrescente

if (lista[0] > (lista[1] + lista[2])):
    print('Não é possível formar um triângulo!')
else:
    print('É possível formar um triângulo')

# OU ######################################################################################################
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1+ n2:
    print('É possível formar um triângulo')
    # Exercício 42 ########################
    if n1 == n2 == n3:
        print(' O trinangulo é equilátero')
    elif (n1 == n2 != n3) or (n1 == n3 != n2) or (n2 == n3 != n1):
        print(' O triangulo é isóceles')
    else:
        print(' O triangulo é escaleno')
    ########################################
else:
    print('Não é possível formar um triângulo!')