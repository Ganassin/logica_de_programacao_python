# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')
nome3 = input('Digite outro nome: ')
nome4 = input('Digite outro nome: ')

lista = [nome1, nome2, nome3, nome4] # Cria uma lista com todos os nomes digitados

sorteio = random.choice(lista)
print(f'O escolhido foi: {sorteio}!')

random.shuffle(lista) # Embaralha a lista
print(f'Os nomes embaralhados ficam assim: {lista}')