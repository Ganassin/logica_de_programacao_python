''' ------------------------- TEORIA -------------------------------------------

            Aula 16 - Variáveis Compostas -> TUPLAS

    Em Python existem três tipos de ***variáveis compostas***, as TUPLAS (), que
serão vistas nesta aula, as LISTAS [] e os DICIONÁRIOS {};
    As TUPLAS e as LISTAS são estruturas bem semelhantes, porém as LISTAS tem
algumas vantagens que serão vistas nas próximas aulas (são mutáveis).

    As VARIÁVEIS COMPOSTAS são variáveis que podem guardar vários valores:
  * As TUPLAS, guardam uma quantidade delimitada de argumentos, sendo essa
quantidade especificada na hora da sua criação;

    ex: lanche = (hamburguer, refri, pizza, pudim)
                      0         1      2      3
        - print(lache[0]) -> hamburguer
        - print(lanche[0:2]) -> hamburguer, refri
        - print(lanche[1:]) -> suco, pizza, pudim
        - print(lanche[-1]) -> pudim # Primeiro de trás para frente
        - len(lanche) -> 4 # Tamanho da variável

    As TUPLAS são IMUTÁVEIS durante a execução do programa, a partir
do momento em que um item é estabelecido ele não pode ser alterado.

    Os valores da TUPLA podem ser inserídos pelo usuário, colocando um ou mais imput nela,
esse valor inserido pelo usuário só não pode ser mudado depois de estabelecido.

---------------------------- PRÁTICA -----------------------------------------
'''

lanche = ('hamburger', 'refrigerante', 'Pizza', 'Pudim') # Essa é a forma de declarar uma TUPLA

print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-1])

#lanche[1] = 'Soco' # Caso execute essa linha dará erro pois TUPLAS são imutáveis

# FOR percorrendo toda a TUPLA
print('-='*30)
for c, comida in enumerate(lanche):                    # Isso é igual a: for c in range(0, len(lanche))
    print(f'Eu vou comer {comida} na posição {c}')     #                     print(lanche[c])
print('Comi muito!')
# OU                                              # As duar formas funcionam, a melhor vai depender do contexto
print('-='*30)
for c in range(0, len(lanche)):
    print(f'{lanche[c]} na posição {c}')
# OU, sem ter a posição
print('-='*30)
for comida in lanche:
    print(f'Vou comer {comida}!')
print('-='*30)

print(sorted(lanche)) # Este comando mostra a TUPLA em ordem alfabética,
print('-=' * 30)      # para isso transforma em uma LISTA e muda as posições. Isso é visto pelos [] no resultado

a = (2, 5, 4)
b = (3, 5, 1)
c = a + b            # Junta uma TUPLA com a outra
print(c)
print(f'O número 5 aparece {c.count(5)} vezes nos {len(c)} valores presentes na tupla')
print(f'Em que posição está o 4? {c.index(4)} (começando a contar do 0)')
print('-=' * 30)

# As TUPLAS aceitam vários tipos de váriáveis
pessoa = 'gabriel', 24, 'M', 77.54 # Aqui por exemplo foi criada uma TUPLA com info. de uma pessoa.
         # nome, idade, sexo, peso
print(pessoa)
del(pessoa) # TUPLA excluida da memória

# Inserido pelo usuário
numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')))
print(numeros)