media1 = float(input('Digite a primeira nota do aluna (0 a 100): '))
media2 = float(input('Digite a segunda nota do aluna (0 a 100): '))

media = (media1 + media2)/2

if media < 50:
    print(f'Você está reprovado, sua média é {media:.2f}')
elif 50 <= media < 70:
    print(f'Você está de recuperação, sua média é {media:.2f}')
else:
    print(f'Você está aprovado, sua média é {media:.2f}')

