# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra A aparece {frase.count("A")} vezes na frase.\n'
      f'A primeira está na posição {frase.find("A") + 1}\n'  #.find() busca a primeira ocorrência
      f'E a última está na posição {frase.rfind("A") + 1}')  #.rfind() busca a ocorrência mais à direita

