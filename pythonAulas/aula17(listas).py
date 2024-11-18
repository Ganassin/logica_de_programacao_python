'''                             TEORIA (LISTAS)

    Como vimos na última aula, as TUPLAS são IMUTÁVEIS, ou seja, depois que um valor
é colocado em uma posição da TUPLA, ele não pode ser alterado (na execução do código),
caso tente, dará erro

    Para poder fazer essas mudanças em valores de uma determidada posição apenas,
devemos usar uma LISTA.

    Em Python, há vários comandos para manipulação de valores em variáveis
    compostas (LISTAS).

    Para declarar uma LISTA, usamos os "colchetes" -> []
        - lista = [valor1, valor2, ...]
    Diferente das TUPLAS que usamos parênteses -> ()

    Ou podemos declarar uma lista de números usando o método LIST() junto com o RANGE():
        - lista = list(range(x, y))

    Além da funcionalidade de mudar valores, nas LISTAS também podemos ADICIONAR
E EXCLUIR valores. Para isso devemos usar comandos especiais (métodos):

    * Para ADICIONAR NO FINAL da LISTA usamos o .APPEND(): lista.append(novo item)
    * Para ADICIONAR ENTRE X e Y, usamos o método .INSERT(): lista.insert(posição Y, novo item)
    * Para EXCLUIR o item de uma posição qualquer podemos usas os comandos DEL ou .POP():
                                                              del lanche[3] OU lanche.pop(3)
          - O comando .pop(), sem nada no parênteses, remove o último.
          - Comando de EXCLUIR onde não se passa a posição, mas sim o conteúdo (.REMOVE)

    OBS: Se eu criar uma lista A, com valores, e depois criar uma lista B que recebe A (B = A)
    Essas listas ficam com uma "LIGAÇÃO", se eu alterar um valor de uma delas, tbm altera na outra
    Para que se crie um CÓPIA DE UMA LISTA precisamos fazer o seguinte comando:
        - B = A[:] (assim B recebe todos os valores de A, se alterá-los caso altere um valore de A)
'''

# Declara a LISTA ------------------------------------------------------------------------------
lanche = ['Hamburguer', 'Soco', 'Pizza', 'Pudim']
print(lanche)

# DECLARANDO com o método LIST()
valores = list(range(1, 9))
print(valores)
valores.sort(reverse=True)
print(valores)
valores.pop() # remove o último valor da lista
print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} há o valor {v}!')
print('Cheguei ao fim!')

# Mudando um dos valores da LISTA --------------------------------------------------------------
print('\nCOMANDOS DE ALTERAR')
lanche[3] = 'Picolé'
print(lanche)

# Adicionando no final ------------------------------------------------------------------------
print('\nCOMANDOS DE ADICIONAR')
lanche.append('Batata')
print(lanche)

# Adicionando em uma posição especificada
lanche.insert(2, 'Refri')
print(lanche)

# Comando mais básico de excluir. Excluio a posição 5 -----------------------------------------
print('\nCOMANDOS DE EXCLUIR')
del lanche[5]
print(lanche)

# Outro comando de EXCLUIR. O .POP()! (sem parâmetro, elimina o último)
lanche.pop(2)
print(lanche)

# Comando de EXCLUIR onde não se passa a posição, mas sim o conteúdo (.REMOVE)
lanche.remove('Picolé')
print(lanche, '\n')

'''                                  PRÁTICA                                             '''
print('Valores inserídos pelo usário')
del(valores)

# Comando para o usuário inserir valores na lista (FOR)
valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
# OU

# Mesmo comando com COMPREENÇÃO DE LISTAS:
valores = [int(input('Digite: ')) for c in range(0, 5)]
print(valores)

''' --------------------------------------------------------------------------------------------------------------------
Anotações observadas no exercício 74 - TÉCNICA DE COMPREENÇÃO DE LISTAS:

    Essa técnica se trata de crias listas através de expreções, que percorrem intervalor por meio de um FOR
por exemplo, para criar uma lista com os valores da taboada do 9:
        - taboada = [x*9 for x in range(10)]

https://www.youtube.com/watch?v=M2zL6LnQwkw&ab_channel=HashtagPrograma%C3%A7%C3%A3o
'''
taboada = [x*9 for x in range(11)]
print('\nTaboda com COMPREENÇÃO DE LISTAS')
print(taboada)

# que é a mesma coisa que:
multiplicadores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
taboada = []
for v in multiplicadores:
    taboada.append(v * 9)
print('Taboda sem COMPREENÇÃO DE LISTAS')
print(taboada)

'''
    Outro exemplo, agora mostrando os valores pares da lista "valores" que foi criada a cima:
'''
pares = [v for v in valores if v % 2 == 0]
print('\nPares de uma lista (com COMPREENÇÃO DE LISTAS)')
print(pares)

'''
    Outro, criando uma LISTA de TUPLAS, combinando os valores de duas LISTAS
'''
produtos = ['Arroz', 'Feijão', 'Batata']
preço = [7.50, 4.67, 5]
# Nesse caso o exemplo não fez sentido pois essa COMPREENÇÃO DE LISTAS, combinou todos os valores
# de uma lista, com todos os valores da outra, retornando 9 combinações (pois há duas listas com 3 itens)
prod_preco = [(x, y) for x in produtos for y in preço]
print('\nLista de produtos e preços\n', prod_preco)

'''
    Para strings: criar uma lista com as palávras de uma frase
'''
frase = 'Eu gosto de programar em Python'
palavras = [x for x in frase.split()]
print(f'\nA frase "{frase}" tem as palavras:\n', palavras)
