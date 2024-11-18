'''
Normalmente, em outras limguagens de programação, existem três tipos de estruturas de controle/repetição:
 * WHILE
 * FOR
 * REPEAT (DO WHILE)

No caso do PYTHON, exite apenas o FOR e o WHILE, porém, podemos simular a estrutura do REPEAT existente em outras
limguagens de programação.

- Uma forma diferente de usar o WHILE é fazendo um While infinito, que roda até que um comando que o interrompa seja
executado, tal comando é o BREAK. Podemos usar dessa forma:

    while True:
        if condição1:
            ação1
            ação2
        elif condição2:
            ação3
        elif condição3:
            ação4
            break #(esse break "quebra/interrompe" o while e vai direto para a ação final)
    ação final

------------------------------------------------ PRÁTICA --------------------------------------------------------------
'''

# Exemplo de como estamos parando o WHILE até antes dessa aula
n = s = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    s += n
print(f'Você parou! A soma é {s}\n')
# ou
'''n = 0
cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1
print('Parou após 5 números digitados!\n')'''

# Nova forma de parar/interromper o WHILE
n = s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
print(f'Você parou! A soma é {s:_^10}\n') # :^10 centraliza em 10 espaços

'''Isso pode ser uma ótima alternativa em exercícios que apresentem um menu com a opção "sair" por exemplo,
   caso o usuário escolha sair, o break é executado e o while True acaba'''