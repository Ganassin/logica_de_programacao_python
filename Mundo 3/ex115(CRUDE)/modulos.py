def menu():
    print('-'*30)
    print('MENU PRINCIPAL'.center(30))
    print('-'*30)

    print('\033[0;32m 1 \033[m- \033[0;33mVer pessoas cadastradas\033[m')
    print('\033[0;32m 2 \033[m- \033[0;33mCadastrar nova pessoa\033[m')
    print('\033[0;32m 3 \033[m- \033[0;33mSair\033[m')
    print('-'*30)

    while True:
        try: 
            opcao = leiaInt('Digite uma opção: ')
        except (TypeError, ValueError):
            print('\033[0;31mOpção inválida!\033[m')
            continue
        else:
            if opcao not in (1, 2, 3):
                print('\033[0;31mOpção inválida!\033[m')
                continue     
            else:
                return opcao
                break



def leiaInt(msg):
    while True:
        # Com o TRY EXCEPT
        try: 
            var = int(input(f'{msg}'))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return '#N/A'
        else:
            if var in (1, 2, 3):
                return var
                break
            else:
                print('\033[0;31mOpção inválida! Veja o menu!\033[m')