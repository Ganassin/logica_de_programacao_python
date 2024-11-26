# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Variáveis usadas para calcular a média de idade
soma_idade = 0
cont_media = 0
# Variável usada para armazenar a maior idade digitada para um homem
homem_velho = 0
nome_velho = ''
# Variável usada para contar quantas mulheres com menos de 20 anos
cont_mulheres = 0

for c in range(1,3):
    print(f'----- {c}ª Pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): '))

    soma_idade += idade
    cont_media += 1

    if sexo in 'Mm' and idade > homem_velho: # o "in" considera: se sexo fou igual a M ou m ---------------------------
        homem_velho = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        cont_mulheres += 1

print('\n', '-'*40)
print(f'A média de idade do grupo é de {soma_idade/cont_media:.2f} anos')
print(f'O homem mais velho tem {homem_velho} anos e se chama {nome_velho}')
print(f'Ao todo temos {cont_mulheres} mulher(es) com menos de 20 anos')
print(' ','-'*40)