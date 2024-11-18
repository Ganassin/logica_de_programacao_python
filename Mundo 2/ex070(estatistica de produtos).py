print('-'*20)
print('        Loja X      ')
print('-'*20)

produto = nome_barato = ' '
preco = soma = cont = c = barato = 0

while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: '))

    soma += preco

    if preco > 1000:
        cont += 1
    
    c += 1
    if c == 1 or preco < barato:
        barato = preco
        nome_barato = produto

    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print('---------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {cont} produto(s) custando mais de R$1.000,00!')
print(f'O produto mais barato foi "{nome_barato}" que custou R${barato:.2f}')