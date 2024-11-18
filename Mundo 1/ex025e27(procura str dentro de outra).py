nome = str(input('Qual o seu none completo? ')).strip().lower()

print(f'Você tem Silva no nome? {nome[nome.find("silva"):(nome.find("silva") + 5)] == "silva"}')
# ou
print(f'Você tem Silva no nome? {"silva" in nome}')

print(f'Seu primeiro nome é {nome[:nome.find(" ")].title()} e seu último nome é '
      f'{nome[nome.rfind(" "):].title()}')
# ou
print(f'Seu primeiro nome é {nome.split()[0]} e o último é {nome.split()[-1]}')