# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                                
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)

# FUNÇÕES
def analisa_notas (lista_notas, situ=True):
    dados = {
        'maior': max(lista_notas),
        'menor': min(lista_notas),
        'media': round(sum(lista_notas)/len(lista_notas),2)
    }

    if situ == True:
        if dados['media'] >= 7:
            dados['situação'] = 'Boa'
        else:
            dados['situação'] = 'Ruim'
    
    return dados

# CÓDIGO PRINCIPAL
alunos = {
    'indice':[],
    'nome':[],
    'nota1':[],
    'nota2':[],
    'media':[]
}
indice = 0

while True:
    
    alunos['indice'].append(indice)
    alunos['nome'].append(str(input('Nome do aluno: ')).strip().title())
    alunos['nota1'].append(float(input('Nota 1: ')))
    alunos['nota2'].append(float(input('Nota 2: ')))
    alunos['media'].append( ((alunos['nota1'][indice]+alunos['nota2'][indice])/2) )
    

    escolha = str(input('Deseja adicionar mais dados? [S/N] ')).strip().upper()
    if escolha not in 'SN':
        escolha = str(input('Deseja adicionar mais dados? [S/N] ')).strip().upper()
    elif escolha in 'S':
        indice += 1
    elif escolha in 'N':
        break

print(f'Dados dos alunos: \n{alunos}\n')
print( f'Dados da primeira prova: \n{analisa_notas(alunos["nota1"])}' )
print( f'Dados da segunda prova: \n{analisa_notas(alunos["nota2"], situ=False)}' )