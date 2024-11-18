cont_abre = cont_fecha = 0

expresao = str(input('Digite uma expresão: '))

for termo in expresao:
    if termo == '(':
        cont_abre += 1
    elif termo == ')':
        cont_fecha += 1

if cont_abre == cont_fecha:
    print('Expresão validada!')
else:
    if cont_abre > cont_fecha:
        print('Espresão inválida, falta fechar um parênteses!')
    elif cont_fecha > cont_abre:
        print('Espresão inválida, há um parênteses desnecessário!')

# Feito na aula

pilha = list()

for termo in expresao:
    if termo == '(':
        pilha.append(termo) # adiciona na pilha
    elif termo == ')':
        if len(pilha) > 0:
            pilha.pop()     # retira da pilha
        else:
            pilha.append(termo)

if len(pilha) == 0:
    print('Expresão válida!!!')
else:
    print('Expresão Inválida!!!')


