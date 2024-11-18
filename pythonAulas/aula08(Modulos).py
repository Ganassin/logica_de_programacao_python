# Nesta aula aprendemos como estender a linguagem Python, como colocar mais funcionalidadee (modulos)
# além do que ja vem de fábrica.

# Para adicionar novos módulos utilizamos o comando "import" seguido do nome do módulo, nas primeiras
# linhas do código.
# Caso não seja necessário importar todas as funções de um módulo, podemos usar o comando
# "from módulo import função específica"

# Veja um exemplo real:
'''

import math #importo toda a biblioteca math
n1 = int(input('Digite um número: '))
raiz = math.sqrt(n1) #Usando uma função da biblioteca math, sqrt() calcula a raiz

print(f'A raiz de {n1} é {raiz:.2f}, que arredondado para cima é {math.ceil(raiz)}!') #Função ceil() arredonda o número para cima!

'''


#Para importar somente a função sqrt() e ceil() da biblioteca math o código fica um pouco diferente
from math import sqrt, ceil
n1 = int(input('Digite um número: '))
raiz = sqrt(n1) #Usando uma função da biblioteca math, sqrt() calcula a raiz

print(f'A raiz de {n1} é {raiz:.2f}, que arredondado para cima é {ceil(raiz)}!')

# Link da documentação da bibliotaca math: https://docs.python.org/3/library/math.html
# Link da documentação das bibliotecas: https://docs.python.org/3/library/index.html


