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
        print()
        print('-'*30)
        print(f'Opção 1'.center(30))
        print('-'*30)
        # Abrir o arquivo para leitura
        with open(nome, 'rt') as arquivo:
            # Iterar por cada linha do arquivo
            for linha in arquivo:
                # Remover espaços em branco e quebras de linha
                linha = linha.strip()
                # Dividir os dados por ponto e vírgula
                nome, idade = linha.split(';')
                # Exibir o nome e idade no formato desejado
                print(f'Nome: {nome}'.ljust(15), end='') 
                print(f'Idade: {idade}'.rjust(15))
    finally: 
        a.close()


def cadastrar(arquivo, nome='#N/A', idade=0):
    print()
    print('-'*30)
    print(f'Opção 2'.center(30))
    print('-'*30)

    try:
        a = open(arquivo, 'at') # at significa append/adicionar em arquivo de texto
    except:
        print('\nHouve um erro na abertura do arquivo!\n')
    else:
        try:
            a.write(f'\n{nome}; {idade}')
        except:
            print('Erro ao escrever os dados!')
        else:
            print('Dados cadastrados !!!\n')
        

        