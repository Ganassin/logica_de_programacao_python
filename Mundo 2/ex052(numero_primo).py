''' ------------------------------- CÓDIGO COM IMPORTAÇÃO --------------------------------------------
from colorama import Fore, init

# Inicia o colorama
init()

num = int(input('Digite um número inteiro: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        print(Fore.GREEN, str(c), end=' ')
        cont += 1
    else:
        print(Fore.RED, str(c), end=' ')
# Volta para a cor padrão
print(Fore.RESET)

print(f'O número {num} foi divisível {cont} vezes!')
if cont==2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
'''

''' ----------------------- CÓDIGO COM CORES SEM IMPORTAÇÃO (PADRÃO ANSI) ----------------------------------------- '''
num = int(input('Digite um número inteiro: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m', str(c), end=' ')
        cont += 1
    else:
        print('\033[31m', str(c), end=' ')

# Valta para a cor padrão
print('\033[m')

print(f'O número {num} foi divisível {cont} vezes!')
# IF com a lógica para saber se é primo (divisível somente por 1 e ele mesmo) ou não
if cont==2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')