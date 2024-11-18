''' --------------------------------- Primeira aula do MUNDO 2 DE PYTHON ------------------------------------------ '''
''' 
   - Aula 11.2 - Dicas e Regras:
   No mundo 2 veremos as estruturas de controle, condições e laços. São dois assuntos principais, condições simples,
   compostas e alinhadas e iterações, que são as estruturas de repetição com variáveis de controle, com teste lágico 
   no início e repetições infinitas com interrupção no meio.
                                                     
   - AULA 12 - Condições Aninhadas:
***  Uma estrutura aninhada e colocar uma estrutura condicional e colocar dentro de outras estruturas condicionais  ***
   por exemplo:
    if condição:                        if condição:
        ação                                ação
    else:                               elif condição:
        if condição:          OU            ação
            ação                        else:
        else:                               ação
            ação
   
   A segunda estrutura é mais simplificada, com ela podemos usar quantos "elif" precisar
   Ex:
'''
nome = str(input('Qual o seu nome? ')).strip().title() # strip() tira espaços desnecessários
                                                       # title() deixa a(s) primeiras letras maiúsculas
if nome == 'Gabriel':
    print(f'Que nome bonito {nome}!')
elif nome == 'Paulo' or nome == 'Ana':
    print(f'Não gosto de você {nome}!')
elif nome == 'Maria Gabriela':
    print(f'Você é linda {nome}!')
else:
    print(f'Vá embora {nome}!')