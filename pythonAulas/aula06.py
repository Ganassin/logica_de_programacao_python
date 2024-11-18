num1 = int(input('Digite um número: '))
print(f'O valor digitado é do tipo {type(num1)}\n')
num2 = int(input('Digite outro número: '))
print(f'O valor digitado é do tipo {type(num2)}\n')

soma = num1 + num2
subtrai = num1 - num2
multiplica = num1 * num2

print(f'A soma entre {num1} e {num2} é {soma}, a subtração é {subtrai} e a multiplicação é {multiplica}.')

# Os tipos primitivos são:
#   * int( ) = números inteiros; (1, 5, 15)
#   * float( ) = números reais (pontos flutuantes); (2.5, 34.52, 7.0)
#   * bool( ) = Valores lógicos ou buleanos (True ou False);
#   * str( ) = caracteres, letras;

a = input('Digite algo: ')
print(a.isnumeric())

