# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# Função do ex104
def leiaInt():
    while True:
        # Com o TRY EXCEPT
        try: 
            var = int(input('\nDigite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return '#N/A'
        else:
            return var
            break

        # Sem o TRY EXCEPT, como foi feito no ex 104.
        # Com essa opção não é possível dar diferentes tratamentos para cada tipo de erro
        '''var = str(input('Digite um número: '))
        if var.isnumeric() == False:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
            continue
        else: 
            return int(var)
            break'''

def leiaFloat(msg):
    while True:
        try: 
            var = float(input(f'\n{msg}'))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número float válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return '#N/A'
        else:
            return var
            break

n = leiaInt()
print(f'\nVocê digitou o número inteiro: {n}')

f = leiaFloat('Digite um número real: ')
print(f'\nVocê digitou o número real: {f}')