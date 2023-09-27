- .isdigit()
False se tem algo q nao é numero
true se tudo é numero

- .isinstance(variavel,type)
False se nao for do tipo ou classe q ta no segundo argumento
True

- Try / except: ValueError:
    try:
        numReal = float(numReal)
    except ValueError:
        numReal = input("Erro. Digite novamente. Coloque um numero real: ")

- round: arredonda
round (variavel + 0.5) - pra cima
round (variavel - 0.5) - pra baixo
round (1.333 , 2) - arredonda com 2 casas decimais