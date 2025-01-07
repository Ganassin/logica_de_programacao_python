import modulos
from arquivo import arqExiste, criaArquivo, lerArquivo, cadastrar
from time import sleep

arq = 'ex115_nomes.txt'
if not arqExiste(arq):
    criaArquivo(arq)


while True:
    sleep(1)
    opcao = modulos.menu()

    if opcao == 1:
        lerArquivo(arq)
    
    elif opcao == 2:
        print('NOVO CADASTRO'.center(30))
        nome = str(input('Nome: ')).strip().capitalize()
        idade = modulos.leiaInt('Idade: ') 
        cadastrar(arq, nome, idade)
    
    elif opcao == 3:
        print()
        print('-'*30)
        print(f'Opção {opcao}'.center(30))
        print('-'*30)
        print('Saindo do sistema, até logo!')
        break

