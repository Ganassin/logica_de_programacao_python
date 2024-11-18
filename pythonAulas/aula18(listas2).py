''' ------------------------ Aula 18 - LISTAS Parte 2 ----------------------------
                                     TEORIA

Declaração de LISTA:
    nome_lista = list()
    nome_lista = []

Nesta aula vamos ver que é criar uma lista de listas (LISTAS COMPOSTAS), onde cada elemento da lista principal pode ser
uma outra lista. Um exemplo desse esquema é criar uma lista com dados de pessoas, onde pessoas é a
principal, e dentro dos seus elementos há listas de dados, como nome e idade.

    pessoas = [['Gabriel',24], ['Maria',22], ...]
                   0      1        0    1
                    0                1       2

Para mostrar um elemento de um elemento da lista pessoas, usamos:
    print(pessoas[0][0]) - 'Gabriel'     ou     print(pessoas[1][1]) - 22

Para deixar essa estrutura mais detalhada, com informações mais claras, como nome de índices por exemplo, o mais
próximo possível de uma estrutura de dados como um banco de dados.
    (ex: chamar o indice 0 do índice 0 da lista pessoas de nome e o índice 1 do 0 de idade)

                                  PRÁTICA
'''

teste = []

teste.append('Gabriel')
teste.append('24')
print(teste)

pessoas = [teste]
print(pessoas)

teste2 = ['Maria', 22]
pessoas.append(teste2)
print(pessoas)

# Uma forma mais eficiente de receber dados de pessoas e colocar em uma lista
dados = ['Astolfo', 65]
outras_pessoas = []
outras_pessoas.append(dados[:]) # Insere uma cópia dos dados de dados, para que eles não mudem dentro da outras_pessoas nos próximos passos

dados = ['Penelope', 54]
outras_pessoas.append(dados[:])

print(outras_pessoas)
print(outras_pessoas[0])
print(outras_pessoas[1][0])

for p in outras_pessoas:
    print(f'{p[0]} tem {p[1]} anos!')

nomes = [dados[0] for dados in outras_pessoas]
print(nomes)
idade = [dados[1] for dados in outras_pessoas]
print(idade)

# Recebendo os dados do usuário
dados.clear()
outras_pessoas.clear()
# Lê dados e joga dentro de uma lista
for c in range(0, 3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    outras_pessoas.append(dados[:])
    dados.clear()
print(outras_pessoas)

# Analisa dados lidos
print('Maiores de idade:')
for p in outras_pessoas:                       # p é cada registro da lista "outras_pessoas", ou seja, nome[0] e idade[1]
    if p[1] >= 18:                             # p[1] é o 1 de cada registro, ou seja, a idade
        print(f'{p[0]} é maior de idade!')     # p[0] é o nome
