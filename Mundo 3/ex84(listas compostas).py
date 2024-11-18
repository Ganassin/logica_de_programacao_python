pessoas = [] # armazena nomes e pesos digitados (listas dentro de lista)
dados = [] # Recebe um nome e um peso
while True:
    dados.append(str(input('Nome: ')).strip()) # Recebe um nome e retira espaços desnecessários (strip)
    dados.append(float(input('Peso: ')))       # Recebe um peso
    pessoas.append(dados[:])                   # Adiciona uma cópia da lista dados na lista pessoas
    dados.clear()                              # limpa a lista dados

    escolha = input('Quer continuar? [S/N]').strip().upper()
    while escolha not in 'SN':
        escolha = input('Quer continuar??? [S/N]').strip().upper()
    if escolha == 'N':
        break

print('-='*30)
print(f'{len(pessoas)} foram cadastradas!')  # Conta quantas listas com nome e peso há na lista pessoas

mais_pesado = mais_leve = 0
for pos, p in enumerate(pessoas):
    if pos == 0:
        mais_pesado = mais_leve = p[1]
    else:
        if p[1] > mais_pesado: # p é uma das listas dentro da lista pessoas, o 1 é o segundo elemento dessa lista (peso)
            mais_pesado = p[1]
        elif p[1] < mais_leve:
            mais_leve = p[1]

print(f'O maior peso foi de {mais_pesado} Kg, sendo de {[p[0] for p in pessoas if p[1] == mais_pesado]}')
print(f'O menor peso foi de {mais_leve} Kg, sendo de {[p[0] for p in pessoas if p[1] == mais_leve]}')

'''max(pessoas, key=lambda p: p[1])
    min(pessoas, key=lambda p: p[1])
    
    pessoas_pesadas = [p[0] for p in sorted(pessoas, key=lambda p: p[1], reverse=True)]
    print(f'As duas pessoas mais pesadas: {pessoas_pesadas[:2]}')
    
    pessoas_leves = [p[0] for p in sorted(pessoas, key=lambda p: p[1])]
    print(f'As duas pessoas mais leves: {pessoas_leves[:2]}')'''
