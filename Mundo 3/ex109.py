# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from modulos import moeda_109

preco = float(input('\nDigite um valor: R$ '))

print(f'\nO dobro de {moeda_109.moeda(preco)} é {moeda_109.dobro(preco, format_moeda=True)} e a metade é {moeda_109.metade(preco, format_moeda=True)}!')
print(f'O valor com um desconto de 15% é { moeda_109.diminuir(preco, 15, True) }')
print(f'O valor com um aumento de 30% é { moeda_109.aumentar(preco, 30, True) }')