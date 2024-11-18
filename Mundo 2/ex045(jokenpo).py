import time, random # importação de bibliotecas para espera e sortear
print('='*35,' JOKEMPO! ', '='*35)
print('Escolha uma das opções abaixo:\n'
      '[0] Pedra\n'
      '[1] Papel\n'
      '[2] Tesoutra\n')
escolha = int(input('Qual a sua escolha? '))

print('=-'*40)
time.sleep(1)
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO!!!')
time.sleep(0.5)

lista = ['Pedra', 'Papel', 'Tesoura'] # cria uma lista com os três itens
sorteio = random.choice(lista)        # sorteia um dos itens da lista, o resultado é o nome

print('=-'*40)
if ((escolha == 0 and sorteio == 'Tesoura')
        or (escolha == 1 and sorteio == 'Pedra')
        or (escolha == 2 and sorteio == 'Papel')):
    print('Você Ganhou !!!')
elif escolha == lista.index(sorteio): # lista.index(sorteio) pega qual o indice da lista referente ao nome sorteado
    print('Empate!!!')
elif escolha >= 3:
    print('Jogada inválida!!!')
else:
    print('Você Perdeu!!!')
print(f'O computador escolheu {sorteio}!')
print('=-'*40)