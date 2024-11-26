# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

escolha = 0
while escolha != 5:
    # Menu
    print('='*20)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novo números')
    print('[5] Sair')
    print('='*20)

    escolha = int(input('Escolha uma opção (número de 1 a 5): '))
    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}\n')
    elif escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}\n')
    elif escolha == 3:
        if n1 == n2:
            print(f'{n1} e {n2} são iguais\n')
        else:
            print(f'O maior é {max(n1,n2)}\n')
    elif escolha == 4:
        print('Digite os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('\nFinalizando...')
    else:
        print('Opção inválida, escolha uma correta!/n')
print('FIM!')