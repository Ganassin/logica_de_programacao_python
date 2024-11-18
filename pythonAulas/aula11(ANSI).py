''' Nesta aula vamos ver um pouco sobre o padrão ANSI, mais especificamente adicionando cores aos resultados dos
    códigos

    ANSI é um padrão de normalização internecional, que tem ecape sequence (funciona em vários ambientes)
    * Ele se inicia com uma contra barra seguida de um código, com por exemplo:
        - \n: Pula linha
        - \033[ style; text; background  m : formata o texto
        ex: \033[0;33;44m :
            style: 0 (nada); 1 (negrito); 4 (sublinhado); 7 (negativo)
            text: cores do texto, variam de 30 a 37 (branco, vermelho, verde, amarelo, azul...)
            Background: cores de fundo, que variam de 40 a 47

    '''

print('\033[1;31;44mteste\033[m')