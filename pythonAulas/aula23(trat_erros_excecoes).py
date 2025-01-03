'''
  -------------------------------------  TRATAMENTO DE ERROS E EXCEÇÕES  ------------------------------------------
  Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. 
  Aprenda como usar a estrutura try except no Python de uma forma simples.

  - Quando temos um erro que não se da de forma sintática, ou seja, não está escrito errado, normalmente o código funcionaria
  mas não está funcionando. Nesses caso chamamos o erro de EXCEÇÃO.
  Um exemplo é quando tentamos usar uma variável não declarada. A sintáxe do código pode estar correta, mas há erro.
  Ou quando tentamos imputar uma string em um int.

  - Sabendo isso, podemos usar o comando try exept, que é basicamento um "tente isso, se não, mostre a exceção", veja:

  try: 
    """comando"""
  exept:
    """exceção/falha"""
'''
try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um outro número: '))
    div = n1 / n2
except Exception as erro:
    print('\033[0;31mInfelizmente tivemos um problema!\033[m') # mensagem mostrada antes da msg de erro, se não houver o else a seguir!
    print(f'O problema encontrado é da classe: {erro.__class__}')
#except ZeroDivisionError:
#    print('Não é possível dividir por zero!')
#except ValueError:
#    print('Um dos valores digitados não um número inteiro!')
else: 
    print(f'O resultado é {div}')
finally:
    print('FIM!!!')