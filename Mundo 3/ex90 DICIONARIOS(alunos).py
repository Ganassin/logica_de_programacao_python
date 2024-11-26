# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

alunos = {}

alunos['Nome'] = str(input('Qual o nome do aluno? '))
alunos['Media'] = float(input('Qual a média do aluno? [0 a 10] '))

if alunos['Media'] >= 7:
    alunos['situacao'] = 'Aprovado'
else:
    alunos['situacao'] = 'Reprovado'


print(alunos)
print(f'O Nome é {alunos["Nome"]}')
print(f'A média é {alunos["Media"]}')
print(f'A situação é {alunos["situacao"]}')