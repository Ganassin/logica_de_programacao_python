
# Função
def fatorial (var, mostra=False):
    """Calcula o fatorial de um número:
    sendo o primeiro parâmetro o número e o segundo (True or False) para mostrar ou não a conta feita."""

    result = 1
    for c in range(var, 0, -1):
        result *= c
        if mostra == True:
            print(f'{c}', end=' x ')
    
    if mostra == False:
        return result
    elif mostra == True: 
        return f'= {result}'

# Código principal
fat = int(input('Deseja ver o fatorial de qual número? '))
print(f'O fatorial de {fat} é {fatorial(fat, True)}!')

help(fatorial)