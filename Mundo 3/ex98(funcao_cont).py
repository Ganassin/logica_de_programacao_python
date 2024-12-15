# Função
def contador (i, f, p):
    for x in range(i, f, p):
        print(x, end=' ')


# Código Principal
print('\nContagem 1:')
contador(1, 11, 1)

print('\n\nContagem 2:')
contador(10, -1, -2)

print('\n\nContagem 3:')
print('  ESCOLHA')
inicio = int(input('  Início da contagem: '))
fim = int(input('  Fim da contagem: '))
passo = int(input('  Passo da contagem: '))
contador(inicio, fim, passo)