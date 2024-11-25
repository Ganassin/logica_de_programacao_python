# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

print('-'*50, ' CALCULADORA DE HIPOTENUSA ', '-'*50)

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdijacente = float(input('Digite o comprimento do cateto adijacente: '))

# Primeira forma de calcular:
hipot = (catetoOposto**2 + catetoAdijacente**2)**0.5
print(f'A hipotenusa é {hipot:.2f}\n')

# Segunda forma de calcular, com importação:
from math import hypot
print(f'A hipotenusa é {hypot(catetoOposto, catetoAdijacente):.2f}\n')
