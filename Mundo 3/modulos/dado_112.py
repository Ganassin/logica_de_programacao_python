def leiadinheiro(msg):
    valido = False
    
    while not valido:
        preco = str(input(f'\n{msg}')).replace(',','.').strip()
        
        if preco.isalpha() or preco == '':
            print(f'\033[0;31mERRO! {preco} é um preço inválido!\033[m')
        else: 
            valido = True
            return float(preco)    