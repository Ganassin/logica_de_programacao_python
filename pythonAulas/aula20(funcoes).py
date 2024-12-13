'''
Aula 20 - Funções (def) em Python

    Funções em python podem ser associadas a ROTINAS, ou seja, coisas que são feitas constantemente dentro do programa!
    
    Com as funções, escrevemos essa rotina uma vez no início do programa, com o comando DEF, 
    e podemos repeti-la várias vezes durante o código, utilizando seu nome e se houver, o parâmetro entre parênteses.
    Os parâmetros, são "variáveis" usadas dentro da função!

    Com o uso de funções, dividimos o código em dois "blocos", onde o primeiro ficam as funções e o segundo é o programa principal.
    O Python, por padrão, executa as funções que são declaradas logo no início, apenas se elas forem "chamadas" no programa principal.

    No Python, existe a funcionalidade de "EMPACOTAR PARÂMETRO", para usar, na hora de declarar a função usamos um " * " seguido do nome
    da variável onde os parâmetros passados serão armazenados, que sera uma TUPLA. VEJA O EXEMPLO DA FUNÇÃO "somar_numeros" 
    
'''
# FUNÇÕES: ==========================================================================================================================
def titulo (texto):
    print('-'*40)
    print(str.center(texto, 40))
    print('-'*40)

def somar_dois (a, b):
    s = a + b
    print(f'A = {a} e B = {b}')
    print(f'A + B = {s}')

def somar_numeros (*num):
    print(sum(num))

def ordena_num (lista):
    lista = sorted(lista)
    print(lista)

# PROGRAMA PRINCIPAL ================================================================================================================
titulo('Olá mundo')
print()
titulo('Exemplo')
print()

somar_dois(3, 5)
print()
somar_dois(b=5, a=7)
print()

somar_numeros(1,2,3,4,5)
print()

nums = [1, 2, 6, 4, 8, 3]
ordena_num(nums)