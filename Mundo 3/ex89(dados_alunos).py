dados = []
nome = []
notas = []

while True:

    nome.append(str(input('Nome do aluno: ')).strip().title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))

    dados.append(nome[:])
    dados.append(notas[:])

    nome.clear()
    notas.clear()

    escolha = str(input('Deseja adicionar mais dados? [S/N] ')).strip().upper()
    if escolha not in 'SN':
        escolha = str(input('Deseja adicionar mais dados? [S/N] ')).strip().upper()
    elif escolha in 'N':
        break

print('-'*20, ' BOLETIM ', '-'*20)
#print('\n')

for n in range(0, len(dados), 2):
    media = (dados[n+1][0] + dados[n+1][1])/2
    print('Aluno:', dados[n][0], ' '*20, ' Média:', media)

while True:

    escolha = str(input('\nConsultar as notas de algum aluno? [S/N] ')).strip().upper()
    if escolha not in 'SN':
        escolha = str(input('Consultar as notas de algum aluno? [S/N] ')).strip().upper()
    elif escolha in 'N':
        break
    else:
        aluno = str(input('Nome do aluno: ')).strip().title()

    index = [index for index, valor in enumerate(dados) if valor[0] == aluno]
    print(index)
    aluno = ''