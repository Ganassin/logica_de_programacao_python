listagem = ('Pão', 1.00, 'Leite', 3.50, 'Bolo', 17.25, 'Suco', 5.00, 'Pão de queijo', 1.50)

print('-'*40)
print('LISTAGEM DE PREÇOS'.center(30))
print('-'*40)

for x in range(0, len(listagem), 2):
    print(f'{listagem[x]}'.ljust(27, '.'), 'RS', f'{listagem[x+1]:.2f}'.rjust(8))
print('-'*40)

'''
   ljust(espaços, preenchimento): Esta função coloca o texto à esquerda e delimita a quantidade de espaços e 
                                  oque colocar nos vazios
   center(espaços, preenchimento): Faz a mesma coisa e deixa o texto no meio
   rjust(espaços, preenchimento): Faz a mesma coisa e deixa o texto na direita
'''