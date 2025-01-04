def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo!')
    else: 
        print(f'Arquivo {nome} criado!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\nErro ao ler o arquivo\n')
    else:
        print(a.read())
        