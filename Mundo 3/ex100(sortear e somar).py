# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre 
# todos os valores pares sorteados pela função anterior.

# Funções
def sortear(lista): 
    from random import randint
    for c in range(0,5): 
        n = randint(0, 10)
        lista.append(n)

def somaPar(lista):
    soma = 0

    for n in lista:
        if n % 2 == 0:
            soma += n
    
    return soma

# Programa principal
numeros = []

while True:

    num = int(input('\nDigite um número: '))
    numeros.append(num)

    escolha = str(input('Deseja adicionar mais números? [S/N] ')).strip().upper()
    
    while escolha not in 'SN':
        escolha = str(input('\nDigite [S] para sim e [N] para não! ')).strip().upper()
    
    if escolha == 'N':
        break

sortear(numeros)
print(numeros)
print(f'A soma dos números pares é {somaPar(numeros)}')