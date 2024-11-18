'''
    Uma cadeia de texto/caractere nada mais é que uma string. Aprender a manupulá-las é muito importante para evoluir os
conhecimentos em Python.

    Uma string é composta por vários "mini espaços", onde em cada uma há um caractere e cada espaço é identificado por
um índice, veja:

        Olá Mundo!  -> Essa cadeia de caracteres tem 10 caracteres, seus respectivos índices são:
        __________
        0123456789      Obs: esse conjunto de caracteres é tratado como uma lista.

    Devido a essa característica é possível realizar várias operações com uma string, como por exemplo o "FATIAMENTO",
que na mais é que pegar pedaços da string.
    Veja exemplos:
'''

frase = 'Olá Mundo!'
print('+'*30, 'FATIAMANETO', '+'*30)
print(frase)            # Aqui a cadeia de caracteres inteira é mostrada
print(frase[2])         # Aqui apenas o caractere de índice 2 é mostrado
print(frase[0:3])       # Aqui os caracteres de 0 a 2 são mostrados
print(frase[0:9:2])     # Aqui os caracteres de 0 a 8, pulando de 2 em 2, são mostrados
print(frase[:5])        # Aqui mostra do início até o caractere 4
print(frase[4:], '\n')  # Aqui mostra do caractere 4 até o final

'''
    Outra operação possível de ser realizada com strings é a "ANÁLISE", que como o nome diz, analiza algumas informações
da cadeia de caracteres, como por exemplo o tamanho, a primeira letra, etc.
    Veja exemplos:
'''
print('='*30, 'ANÁLISE', '='*30)
print(len(frase))       # Mostra a quantidade de caracteres na string, o tamanho
print(frase.count('o')) # Conta quantos 'o' tem na string. Obs: 'O' e 'o' são diferentes (Case sensitive)
print(frase.count('o',0, 3)) # contagem com fatiamento
print(frase.find('!'))  # Mostra em qual índice um caractere específico está, caso não exista retorna -1
print('Olá' in frase)   # Mostra se existe (True) ou não (False) algo na string

'''
    Outra operação possível de ser realizada com strings é a "TRANSFORMAÇÃO", veja exemplos:
'''
print(frase.replace('Olá', 'Oi')) # Troca 'Olá' por 'Oi'
print(frase.upper())                          # Deixa tudo maiúsculo
print(frase.lower())                          # Deixa tudo minúsculo
print(frase.capitalize())                     # Deixa somento o primeiro caractere maiúsculo
print(frase.title())                          # Deixa a primeira letra de todas as palavrasa em maiúsculo
frase = '  Olá Mundo!    '                # Essa string está com espaços desnecessários ante e depois do texto
frase = frase.strip()                         # Essa função RETIRA ESPAÇOS antes e depois do texto, rstrip() retira
print(frase)                                  # só os da direita e lstrip() só os da esquerda
print(frase.split())                          # Divide a string em uma lista com cada palavra separada
frase = frase.split()
print('-'.join(frase))

'''Dica para dar print em textos grandes'''
print('''texto grandetexto grandetexto grandetexto grandetexto grandetexto grandetexto grandetexto grande
    texto grandetexto grandetexto grandetexto grandetexto grandetexto grandetexto grandetexto grande
    texto grandetexto grandetexto grandetexto grandetexto grandetexto grandetexto grandetexto grande texto grande''')