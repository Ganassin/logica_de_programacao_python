#Função:
def escreva (msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))


# Código principal
mensagem = str(input('Escreva uma mensagem: '))
escreva(mensagem)