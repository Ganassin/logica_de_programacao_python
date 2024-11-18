''' Faça a soma de todos os números ímpares multiplos de três no intervalo de 1 a 500'''

soma = 0
cont = 0

'''for c in range(1, 501):
    if (c % 2 != 0) and (c % 3 == 0):
        print(c, end=' ')
        cont = cont + 1
        soma = soma + c
'''
# OU ------------------------------------------------------------------------------------
for c in range(1, 501, 2): # Faz menas iterações, código melhor
    if c % 3 == 0:
        print(c, end=' ')
        cont = cont + 1
        soma = soma + c

print(f'\nA soma é dos {cont} números ímpares e multiplos de 3 entre 1 e 500 é {soma}')