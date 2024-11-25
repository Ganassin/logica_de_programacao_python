# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO 

media1 = float(input('Digite a primeira nota do aluna (0 a 100): '))
media2 = float(input('Digite a segunda nota do aluna (0 a 100): '))

media = (media1 + media2)/2

if media < 50:
    print(f'Você está reprovado, sua média é {media:.2f}')
elif 50 <= media < 70:
    print(f'Você está de recuperação, sua média é {media:.2f}')
else:
    print(f'Você está aprovado, sua média é {media:.2f}')

