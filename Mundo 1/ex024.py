cidade = str(input('Em que cidade você nasceu? \n'))
cidade = cidade.strip()

print(cidade[:cidade.find(' ')].lower() == 'santo')