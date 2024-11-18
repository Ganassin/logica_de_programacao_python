print('-'*35, ' Calculadora de empréstimo ', '-'*35)

valorCasa = float(input('\nQual o valor da casa que será financiada? '))
salario = float(input('Quanto você recebe por mês? '))
tempo = int(input('Em quantos anos pretende pagar o empréstimo? '))

valorParcela = valorCasa/(tempo * 12)
limiteParcela = salario*0.3

if valorParcela > limiteParcela:
    print(f'Infelismente você não pode parcelar!\n'
          f'O valor da parcela é R${valorParcela:.2f}, isso supera o seu limíte.\n'
          f'   - O valor da casa é muito alto ou o tempo de pagamento é curto!')
else:
    print(f'Você pode parcelar, o valor será R${valorParcela:.2f} mensais durante {tempo*12} meses')