

numero1 = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite um numero inteiro: '))

if numero1 > numero2:
    print(f'O primeiro é maior! {numero1} > {numero2}')
elif numero2 > numero1:
    print(f'O segundo é maior é maior! {numero2} > {numero1}')
else:
    print(f'Os dois são iguais! {numero1} = {numero2}')