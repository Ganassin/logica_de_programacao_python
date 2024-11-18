nome = str(input('Digite seu nome completo: ')).strip()
                                                # strip() remove espaços antes e depois

print(f'Seu nome com todas as letras maiúsculas:\n {nome.upper()}\n')
print(f'Seu nome com todas as letras minúsculas:\n {nome.lower()}\n')
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras!\n')
print(f'O seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')
