# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em que cidade você nasceu? \n'))
cidade = cidade.strip()

print(cidade[:cidade.find(' ')].lower() == 'santo') 
# cidade[:cidade.find(' ')] = cidade[do primeiro caracter até o primeiro espaço]