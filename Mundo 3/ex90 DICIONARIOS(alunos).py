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