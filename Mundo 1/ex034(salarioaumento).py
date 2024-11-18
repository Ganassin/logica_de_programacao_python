salario = float(input('Digite seu salário: '))

if salario > 1250:
    salario = salario * 1.1
else:
    salario = salario * 1.15

print(f'Seu novo salário é de {salario:.2f}')
