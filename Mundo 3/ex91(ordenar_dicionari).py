import random, time

jogadas = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6)
}

# Cria um novo dicionário, ordenando pelo sorted() o dicionário jogadas{}, onde a chave de ordenação é o elemento [1]
# de cada par chave-valor da dict_items([('jogador1', 6), ('jogador2', 6), ('jogador3', 4), ('jogador4', 5)]) (exemplo)
jogadas_ordenadas = dict(sorted(jogadas.items(), key=lambda item: item[1], reverse=True)) # ordena a lista de tuplas de acordo com o valor (item[1]) de cada par chave-valor.

print('Valores Sorteados:')
for key, value in jogadas.items():
    time.sleep(0.5)
    print(f'O {key} tirou {value}')

time.sleep(1)
print('Ranking de Jogadores')
rank = 1
for key, value in jogadas_ordenadas.items():
    print(f'{rank}º Lugar: {key} com {value}')
    rank += 1

''' ------------------------- COMO ORDENAR UM DICIONÁRIO ------------------------------------
   O que é uma função lambda?
Uma função lambda em Python é uma forma rápida de criar uma função "anônima" que você pode usar em uma única linha. 
Pense nela como uma maneira de definir uma função sem ter que usar o def e dar um nome a ela.

   Estrutura da lambda
A estrutura de uma função lambda é: lambda argumentos: expressão

Aqui:
* argumentos é a entrada da função (como os parâmetros de uma função normal).
* expressão é o que a função retorna.

Aplicando ao sorted
No caso de sorted(), o lambda é usado para dizer ao Python como ele deve ordenar os itens. 
O que você passa para key é uma função que o sorted usará para decidir como ordenar os elementos.

Entendendo key=lambda item: item[1]
* item: Este é o argumento que a função lambda recebe. Quando você passa meu_dicionario.items() para sorted(), 
cada item é uma tupla representando um par chave-valor do dicionário. Por exemplo, ('a', 3).
* item[1]: Isso diz à função lambda para pegar o segundo elemento da tupla item. Em uma tupla (chave, valor), 
item[0] seria a chave e item[1] é o valor. Como queremos ordenar pelo valor, usamos item[1].

Exemplo prático:
Dado o dicionário: meu_dicionario = {'a': 3, 'b': 1, 'c': 2}
meu_dicionario.items() retorna: [('a', 3), ('b', 1), ('c', 2)].
Quando sorted() usa a função lambda item: item[1], ele avalia:
Para ('a', 3), item[1] é 3.
Para ('b', 1), item[1] é 1.
Para ('c', 2), item[1] é 2.
sorted() então organiza esses valores em ordem crescente, resultando em uma lista ordenada de tuplas baseada nos valores:

[('b', 1), ('c', 2), ('a', 3)]

Então, a função lambda item: item[1] simplesmente diz a sorted() para usar o valor (item[1]) como a base para a ordenação, e não a chave (item[0]).
'''