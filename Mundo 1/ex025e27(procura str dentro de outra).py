# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual o seu none completo? ')).strip().lower()

print(f'Você tem Silva no nome? {nome[nome.find("silva"):(nome.find("silva") + 5)] == "silva"}')

# ou
print(f'Você tem Silva no nome? {"silva" in nome}')

print(f'Seu primeiro nome é {nome[:nome.find(" ")].title()} e seu último nome é '
      f'{nome[nome.rfind(" "):].title()}')



# ou
# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.
print(f'Seu primeiro nome é {nome.split()[0]} e o último é {nome.split()[-1]}')