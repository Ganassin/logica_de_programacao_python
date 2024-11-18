print('-'*50,' AULA 07 - OPERAÇÕES ARITIMÉTICAS ','-'*50)
n1 = int(input('Digite um número: \n'))
n2 = int(input('Digite outro número: \n'))

# ================================= OPERADORES ARITIMÉTICOS =============================================
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** ou pow(n1, n2) Exponênciação/Potência
# // Divisão inteira
# % Resto da divisão

# =================================== ORDEM DE PRECEDÊNCIA ===============================================
# 1º ()
# 2º **
# 3º *, /, //, %
# 4º +, -
#=========================================================================================================

soma = n1 + n2
sub = n1 - n2
multp = n1 * n2
divs = n1 / n2
exp = n1 ** n2
divInt = n1 // n2
restDiv = n1 % n2

print(f'A soma é {soma:_^11};\n'
      f'A subtração é {sub};\n'
      f'A multiplicação é {multp};\n'
      f'A divisão é {divs}\n'
      f'A exponenciação é {exp} ou {pow(n1, n2)};\n'
      f'A divisão inteira é {divInt};\n'
      f'O resto da divisão é {restDiv};\n'
      )