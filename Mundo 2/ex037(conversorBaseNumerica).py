# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('-'*40,' Conversor de base numérica ','-'*40)

numero = int(input('Digite um numero inteiro que você queira converter: '))
base = str(input('Qual base de conversão, binário, octal ou hexadecimal? ')).strip().lower()

if base == 'binário' or base == 'binario':
    print(bin(numero)[2:])
elif base == 'octal':
    print(oct(numero)[2:])
elif base == 'hexadecimal' or base == 'hexa':
    print(hex(numero)[2:])
else:
    print('Opção inválida!')

'''
Conversão para base binária (base 2):
Para converter um número inteiro para binário, você pode usar o método de divisões sucessivas por 2. 
A ideia é dividir o número inteiro pela base (2, no caso binário) e guardar o resto da divisão. 
Esse resto será o dígito menos significativo do número binário. 
Em seguida, divide-se o resultado inteiro da divisão por 2 novamente, repetindo o processo até que o 
resultado da divisão seja zero. Os restos obtidos ao longo do processo, lidos de baixo para cima, 
formarão o número binário equivalente.

Conversão para base octal (base 8):
A conversão para octal segue um processo similar ao da base binária, mas usando a base 8. Ou seja, 
divide-se o número inteiro por 8 e guarda-se o resto da divisão. Esse resto será o dígito menos 
significativo do número octal. O processo é repetido até que o resultado da divisão seja zero, e os 
restos obtidos formarão o número octal equivalente.

Conversão para base hexadecimal (base 16):
Para converter um número inteiro para hexadecimal, divide-se o número por 16 e guarda-se o resto da divisão. 
Se o resto for maior ou igual a 10, ele é substituído por uma letra (A para 10, B para 11, ..., F para 15). 
Esse processo é repetido até que o resultado da divisão seja zero, e os restos obtidos, lidos de baixo para 
cima, formarão o número hexadecimal equivalente.

Essas são as lógicas básicas para realizar as conversões entre bases numéricas. 
Ao implementar o código em Python, você pode usar operações de divisão inteira (//) e resto (%) 
para realizar as divisões sucessivas e obter os restos. Lembre-se também de que o resultado final 
deve ser apresentado de forma reversa para as bases binária e octal, já que os dígitos menos 
significativos são obtidos primeiro durante o processo de conversão.
'''