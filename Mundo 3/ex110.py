# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from modulos.moeda_110 import resumo

preco = float(input('\nDigite um valor: R$ '))

resumo(preco, 30, 15)
