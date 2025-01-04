import modulos
from arquivo import arqExiste, criaArquivo, lerArquivo
from time import sleep

arq = 'ex115_nomes.txt'
if not arqExiste(arq):
    criaArquivo(arq)


while True:
    sleep(0.5)
    opcao = modulos.menu()

    if opcao == 1:
        print()
        print('-'*30)
        print(f'Opção {opcao}'.center(30))
        print('-'*30)
        lerArquivo(arq)
    
    elif opcao == 2: 
        print()
        print('-'*30)
        print(f'Opção {opcao}'.center(30))
        print('-'*30)
    
    elif opcao == 3:
        print()
        print('-'*30)
        print(f'Opção {opcao}'.center(30))
        print('-'*30)
        print('Saindo do sistema, até logo!')
        break

