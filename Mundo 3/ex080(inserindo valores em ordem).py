# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = list()
valor = cont = 0
escolha = ''

while True:
    valor = int(input('Digite um valor: '))
    if cont == 0:
        valores.append(valor)
        cont += 1
    else:
        if valor > max(valores):
            valores.append(valor)
            print('Adicionado no final da lista!')
        elif valor < min(valores):
            valores.insert(0, valor)
            print('Adicionado no início da lista!')
        else:
            for pos, v in enumerate(valores):
                if valores[pos] < valor < valores[pos+1]:
                    valores.insert(pos+1, valor)
                    print(f'Adicionado na posição {pos+1} da lista!')

    escolha = str(input('Deseja continuar digitando? [S/N] \n')).strip().upper()
    while escolha not in 'SN':
        escolha = str(input('Digite S (sim) ou N (não): \n')).strip().upper()
    if escolha in 'Nn':
        break

print(valores)