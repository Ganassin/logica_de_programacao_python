# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. 
# Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.

'''
MODULARIZAÇÃO - Ato de construir módulos
    - Surgiu com o crescimento e aumento da complexidade dos programas;
    - FOCO: dividir um programa grande (em módulos), aumentar a legibilidade e facilitar a manutenção.

A baixo (exemplo 1) podemos ver como aprendemos até agora, criando as funções dentro do mesmo arquivo, porém, em alguns casos, 
juntando o código principal e todas as funções criadas, fará com que o código inteiro fique muito grande, 
ai é que surge a necessidade da modularização.

Vantagens:
    - Organização, Facilita a manutenção, ocultação de código de funções, reutilização em vários projetos.

PACOTES - uma "além" da modularização, são mais conhecidos como bibliotecas
    Usado quando os módulos ficam grandes de mais.
    Nada mais é que uma junção de módulos (pastas) separados por assuntos. 

    Para cria-los, basta criar uma pasta com os módulos com as funções

'''
# EXEMPLO 1 ----------------------------------------------
def fatorial (n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro (n):
    return n*2

def triplo (n):
    return n*3


num = int(input('Digite um número: '))
fat = fatorial(num)
dob = dobro(num)
trip = triplo(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
print(f'O triplo de {num} é {trip}')
# ========================================================
print()

# EXEMPLO 2 - MODULARIZADO -------------------------------
import aula22_uteis

num = int(input('Digite um número: '))
fat = aula22_uteis.fatorial(num)
dob = aula22_uteis.dobro(num)
trip = aula22_uteis.triplo(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
print(f'O triplo de {num} é {trip}')
# ========================================================