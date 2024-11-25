# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário do funcionário? R$'))
novoSalario = salario * 1.15

print(f'Com o reajuste de 15% ele passará a receber R${novoSalario:.2f}')