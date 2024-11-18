sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] #[0] pega so a primeira letra

# Garante que se o usuário digitar qualquer coisa que não seja M/m ou F/f, ele digite novamente de maneira correta
while sexo not in 'MF': # not in substitui (sexo != 'M' or sexo != 'F')
   sexo = str(input('Dados Inválidos! Por favor, informe seu sexo: ')).strip().upper()[0]

if sexo == 'M':
    print('\nSexo Marculido registrado!')
elif sexo == 'F':
    print('\nSexo Feminino registreado!')
