n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1>n2:
    maior = n1
    if n2<n3:
        menor = n2
    else:
        menor = n3
else:
    if n2>n3:
        maior = n2
        if n1 < n3:
            menor = n1
        else:
            menor = n3
    else:
        maior = n3
        if n1 < n2:
            menor = n1
        else:
            menor = n2

print(f'\nO maior número é {maior}')
print(f'\nO menor número é {menor}')

# OU ####################################
#forma sem if
lista = sorted([n1, n2, n3])
print(f'\n\nO maior número é {lista[2]}')
print(f'\nO menor número é {lista[0]}')