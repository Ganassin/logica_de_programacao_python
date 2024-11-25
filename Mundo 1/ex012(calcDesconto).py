# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o valor do produto? R$'))

print(f'O produto que custava R${preco}, na promoção com desconto de 5% irá custar R${preco*0.95:.2f}.')