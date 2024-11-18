''' -------------------------------------------  TEORIA  -----------------------------------------------------

A estrutura de repetição FOR, é basicamente um "repita no intervalo de X a Y do contador" (for c in range(X, Y))
para o FOR precisamos saber o início e o fim do intervalo, tem uma **VARIÁVEL DE CONTROLE**.

Já o WHILE é uma estrutura de repetição que acontece ENQUANTO uma CONDIÇÃO é verdadeira,
é uma estrutura de repetição com **TESTE LÓGICO**.
Para escrever isso em PYTHON:

    while (CONDIÇÃO):
        ação

    -------------------------------------------  PRÁTICA  -----------------------------------------------------

'''
# Estrutura de repetição com variável de controle =============================================================
for c in range(1, 10):
    print(c)
print('FIM!\n')

# Estrutura de repetição com teste lógico =====================================================================
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!\n')

# Outro exemplo de teste lógico ===============================================================================
r = 'S'
while r == 'S':
    valor = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!\n')

# While para contar números ímpares e pares digitados pelo usuário ============================================
c = 1
par = impar = 0
while c != 0:
    c = int(input('Digite um valor: '))
    if c % 2 == 0:
        par += 1
    else:
        if c != 0:
            impar += 1
print(f'Dentre os números digitados há {par} pares e {impar} ímpares!')
