from datetime import date

print('-'*40,' Calculadorea de Alistamento no Exercito ','-'*40)

ano = date.today().year
nascimento = int(input('Olá jovem, em qual ano você nasceu? '))
idade = ano - nascimento

if idade < 18:
    print(f'Você tem {idade} anos, ainda precisa se alistar um dia! Seu alistamento será em {nascimento + 18}')
elif idade > 18:
    print(f'Você tem {idade} anos, já passou {idade-18} anos do prazo de alistamento, 18 anos!')
else:
    print(f'Você tem {idade} anos, está na hora de se alistar!')

print('\nCategoria de atleta:\n')

if idade <= 9:
    print('Categoria MIRIN')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')
