print('='*50, ' Seno, Cosseno e Tangente ', '='*50)

from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo qualquer: '))
anguloRad = radians(angulo) #Transforma em radianos o andulo digitado em grau

print(f'O seno, cosseno e tangente deste ângulo são: \n'
      f'{sin(anguloRad):.2f}\n'
      f'{cos(anguloRad):.2f}\n'
      f'{tan(anguloRad):.2f}')