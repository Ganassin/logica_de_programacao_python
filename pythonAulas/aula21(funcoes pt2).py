'''
Parte 2 da aula de Funções

Principais tópicos: 
   - Interactive Help (Documentações do Python);
   - Docstrings (Ducumentações das nossas funções);
   - Argumentos/parâmetros opcionais;
   - Escopo de variáveis (quando nascem, morrem, são visíveis, etc.);
   - Funções que retornam resultados;

INTERACTIVE HELP
   É um comando/função de ajuda interativa, o help().
   Para usar digitamos o comando help() e do terminal escrevemos o comando do python que queremos saber mais sobre

DOCSTRIGS
   Uma Docstring é uma string de documentação, é exatamento o resultado do comando help().

   Em casos de criar-mos nossas próprias funções, podemos criar as DOCSTRINGS para elas da seguinte forma:
   ex: def contador (i, f, p):
            """
                DOCSTRINGS
            """
            for x in range(i, f, p):
                print(x, end=' ')
            print('FIM!')

PARÂMETROS OPICIONAIS
    Para usar os parâmetros opcionais usamos o "=" na declaração da função.
    
    ex: " def somar (a, b, c=0): "
        onde c é opicional

    Ou seja, o funcionamento é o seguinte, se tal parâmetro não for passado, 
    o valor considerado será o que foi passado na declaração da função após o "="
    
    Este comando estipula um DEFAULT para a variável

ESCOPO DE VARIÁVEIS
    As variáveis podem ser globais ou locais. Uma função local, é a que foi declarada dentro de uma função, e só pode ser usada lá.
    Já a global é declarada fora da função, no código principal, logo, pode ser usada em qualquer local do código, inclusive em funções.

    Em caso de declarar uma variável com um mesmo nome de forma global e local, o comportamento será de duas variáveis diferentes.
    Para que dentro da função seja considerada a variável declarada fora dela (global), precisamos usar o comando "global nome_var".
    Ou seja, nesse caso precisamos especificar dentro da função que a variável usada é a global.

FUNÇÕES QUE RETORNAM RESULTADOS
    return
    ex:
        def somar (a, b, c):
            s = a + b + c
            return s

'''
# INTERACTIVE HELP
# Ambos os comando a baixo mostram a documentação do comando input()
help(input)
print(input.__doc__)

# DOCSTRINGS
def contador (i, f, p):
    """
    DOCSTRINGS de contador: 
    Faz uma contagem e mostra na tela, sendo:
        i: o primeiro argumento, é o início da contagem;
        f: segundo argumento, é o fim da contagtem;
        p: terceiro argumento, é o passo da contagem;
    """
    for x in range(i, f, p):
        print(x, end=' ')
    print('FIM!')

help(contador)

# PARÂMETROS OPICIONAIS
def somar(a, b, c=0):
    print(a + b + c)

somar(2, 4)

# FUNÇÕES QUE RETORNAM RESULTADOS
def somar (a, b, c):
    s = a + b + c
    return s

print(somar(2, 4, 3))

# ======================================================================================================================================================
# Prática

def fatorial (num=1): # define o default de num como 1
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(fatorial(n))