'''
Nesta aula se inicia o estudo de uma nova categoria de estruturas de controle, as estruturas de repetição.

Aqui veremos os laços, repetições ou iterações.

Primeiro começamos com o FOR (laço com variável de controle)
 - A variavel de controle do for é uma variável que determina o limíte de repetições;
 - Escrevemos da seguinte forma:

    for var_controle range(1,10)
        comando

 - Esse comando significa: "Para o intervalo de 1 a 10 da variável de controle, repita o comando"

 - Dentro da estrutura de repetição podemos colocar outra estrutura, com um if, isso é uma estrutura aninhada
    for var_controle range(1,10)
        if condição
            comando
        comando
'''

print('Oi')
print('Oi')
print('Oi')

print('OU -----------')

# repita para c de 0 a 10 (ORDEM CRESCENTE) --------------------------------------------------------------------------
for c in range(0,5):
    print('Oi')
    print(c)
print('-----------\n')

# repetição de 5 a 0 (ORDEM DECRESCENTE) -----------------------------------------------------------------------------
for c in range(5, 1, -1):
    print(c)
print('-----------\n')

# repetição de 0 a 10 PULANDO DE 2 EM 2 ------------------------------------------------------------------------------
for c in range(0, 11, 2):
    print(c)
print('-----------\n')

# repetição de 0 até o número que o usuário digitar ------------------------------------------------------------------
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('-----------\n')

# repetição com parâmetros fornecidos pelo usiário -------------------------------------------------------------------
inicio = int(input('Começo da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('De quantos em quantos passos? '))
for c in range(inicio, fim+1, passo):
    print(c)
print('-----------\n')