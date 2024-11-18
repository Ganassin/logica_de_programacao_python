a1 = input('Digite algo: \n')

print(f'O que foi digitado é um número? {a1.isnumeric()}')
print(f'O que foi digitado é alfabético? {a1.isalpha()}')
print(f'O que foi digitado é alfanumérico? {a1.isalnum()}')
print(f'O que foi digitado está em minúsculo? {a1.islower()}')
print(f'O que foi digitado está em maiúsculo? {a1.isupper()}')
print(f'O que foi digitado é um espaço? {a1.isspace()}')
print(f'O que foi digitado está capitalizado? {a1.istitle()}')
