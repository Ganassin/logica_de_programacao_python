# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# Biblioteca para remover acentos, foi necessário instalar no terminal
from unidecode import unidecode

# REPLACE: substitui um caractere por outro
frase = str(input('Digite uma frase: ')).replace(' ', '').lower()

# REMOVE ACENTOS
frase = unidecode(frase)

# INVERTE A FRASE DIGITADA E ARMAZENA EM nova_frase
# lan()-1 é pois a contagem começa em 0, se uma frase tem 10 letras (sem espaços) ela vai de 0 a 9
# o segundo -1 é para que o for execute o 0, se colocar 0 no segunto termo, o códio vai ler o c=0 e parar,
# sem executar o comando
nova_frase = ''
for c in range(len(frase)-1, -1, -1):
    nova_frase = nova_frase + frase[c]
# OU
nova_frase = frase[3:1:-1]

print(f'A frase invertida é *{nova_frase}*')
if frase == nova_frase:
    print('Temos um PALÍNDROMO!')
else:
    print('NÃO é palíndromo!')