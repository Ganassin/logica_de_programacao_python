# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

print('='*50, ' Seno, Cosseno e Tangente ', '='*50)

angulo = float(input('Digite um ângulo qualquer: '))
anguloRad = radians(angulo) #Transforma em radianos o andulo digitado em grau

print(f'O seno, cosseno e tangente deste ângulo são: \n'
      f'{sin(anguloRad):.2f}\n'
      f'{cos(anguloRad):.2f}\n'
      f'{tan(anguloRad):.2f}')