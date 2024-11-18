''' -------------------------------------- AULA 19 - DICIONÁRIOS -----------------------------------------------

Com os dicionários, podemos criar estruturas de dados mais completas.

Como por exemplo, em uma lista com nomes e numeros que representam a idade de pessoas, essas informações são
representadas por índices numéricos (0, 1, 2, ...), com os dicionários podemos organizar esses dados, todos
os nomes no índice "nomes" e todas as idades no índice "idade".

DICIONÁRIOS são estruturas de dados semelhantes às TUPLAS e às LISTAS, porém com índices literais.

   * TUPLAS ( )
   * LISTAS [ ]
   * DICIONARIO { } ou dict() - Representados por CHAVES

Para criar:
   * dicionario = {'indice1': 'dado', 'indice2': dado}

Para adicionar elementos nos dicionários:
   * Adisão de um novo índice no dicionário com um valor para esse índice:
      - dicionario['novo_indice'] = 'dado_do_indice'

Para remover elementos
   * Removendo o índice:
      - del dicionario['indice']

Para "pegar" o valor de uma chave de um dicionario:
   * nome_dicionario.get('chave')
   * OU apenas nome_dicionario['chave']

Diferença entra VALOR, CHAVE e ITEM:
   * Valores são os dados presentes em cada índice
      - dicionario.values()
   * Chaves são os títulos dos índices ("indice de uma coluna")
      - dicionario.keys()
   * Os Itens são todos os valores e chaves
      - dicionario.itens()

O conceito de CHAVE, VALOR e ITEM dos dicionários é importante para entender com o FOR em um dicionário funciona:
   * for key, value in dicionario.items(): # Esse exemplo é como usar o enumerate() em listas.
   * for key in dicionario.keys():
   * for value in dicionario.values():

Sabendo dessas características, podemos usar os dicionários nas mais cariadas situações e tbm junto com LISTAS e TUPLAS

OBS: Para pegarmos uma cópia de uma lista, usamos lista[:].
Nos dicionários isso não funciona, usamos o método copy: dicionario.copy()

              ------------- EXTRA ---------------------
------------------------- COMO ORDENAR UM DICIONÁRIO ------------------------------------
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
# exemplo simples
dados = {'nome': 'Gabriel', 'idade': 24} # criação
print(dados['nome'])
print(dados.get('nome'))
print(dados['idade'])

dados['sexo'] = 'M' # adição de um novo índice
print(dados['sexo'])

print(dados)

del dados['sexo'] # exclusão de um índice
print(dados)
print()

# Exemplo com mais sentido
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme)
print(filme.values()) # mostra os valores do dicionário
print(filme.keys()) # Mostra as chaves do dicionário
print(filme.items()) # Mostra os itens do dicionário
print()

for key, value in filme.items():
    print(f'O {key} é {value}!')

print()
'''---------------------------------------- Parte PRÁTICA ------------------------------------------------'''
print('--------------------------- Parte PRÁTICA -----------------------')

# Dicionarios dentro de listas:
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil = [] # LISTA
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print()

# Listas dentro de dicionários
brasil = {
    'uf': ['Rio de Janeiro', 'São Paulo'],
    'sigla': ['RJ', 'SP']
}
print(brasil)
for n in range(0, len(brasil['uf'])):
    print(f'A sigla de {brasil["uf"][n]} é {brasil["sigla"][n]}!')
print()

# dicionáro dentro de listas
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # Adiciona uma copia do dicionario estado na lista em brasil
print(brasil)
for e in brasil:
    print(f'A sigla de {e["uf"]} é {e["sigla"]}!')
