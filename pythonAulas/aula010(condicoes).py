'''  ======================================= AULA 10 - CONDIÇÕES PARTE 01 =============================================
                                             CONDIÇÕES SIMPLES E COMPOSTAS
    * SE (IF)

      if objeto.método():
        BLOCO SE VERDADEIRO
      else
        BLOCO SE FALSO
exemplo:
'''

# CONDIÇÃO COMPOSTA -----------------------------------------
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 5:
    print('\nSeu carro está novo!')
else:
    print('\nSeu carro está velho!')
print('FIM!!!')

# CONDIÇÃO SIMPLIFICADA -------------------------------------
print('\nCarro novo!' if tempo <= 5 else '\nCarro velho!')
print('FIM!!!\n')

print('='*30, 'Média do aluno!', '='*30)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media >= 6.0:
    print(f'\nParabens! Você foi aprovado(a) com média {media:.2f}')
else:
    print(f'\nQue pena, você ficou de recuperação! Sua média foi {media:.2f}')

