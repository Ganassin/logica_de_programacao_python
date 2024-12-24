# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
    while True:
        var = str(input('Digite um número: '))
        
        if var.isnumeric() == False:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
        else: 
            return int(var)
            break

n = leiaInt()
print(f'\nVocê digitou o número {n}')