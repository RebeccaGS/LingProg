
 # add tratamento de erros em primeira eq

# Questão 11
''' Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo . 2A vezes B/2
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
def operacoesBasicas():
    # coletando e convertendo os dados
    primeiroInt = input("Coloque um numero inteiro: ")
    while not (primeiroInt.isdigit()):
        primeiroInt = input("Erro. Digite novamente. Coloque um numero inteiro: ")
    primeiroInt = int(primeiroInt)
    
    segundoInt = input("Coloque outro numero inteiro: ")
    while not (segundoInt.isdigit()):
        segundoInt = input("Erro. Digite novamente. Coloque um numero inteiro: ")
    segundoInt = int(segundoInt)
    
    numReal = input("Coloque um numero real: ")
    try:
        numReal = float(numReal)
    except ValueError:
        numReal = input("Erro. Digite novamente. Coloque um numero real: ")

    numReal = float(numReal)

    # equacoes
    produtoDobro1Metade2 = primeiroInt*2*segundoInt/2
    somaTriplo12 = primeiroInt*3 + numReal
    terceiroCubo = numReal*numReal*numReal

    # prints
    print("Produto do dobro do primeiro com metade do segundo: " + str(produtoDobro1Metade2))
    print("A soma do triplo do primeiro com o terceiro: " + str(somaTriplo12))
    print("O terceiro elevado ao cubo: " + str(terceiroCubo))
    
#operacoesBasicas()

# Questão 12
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def pesoIdeal():
    # coletando e tratando dados
    altura = input("digite sua altura: ")

    for digito in altura:
        if digito == "-":
            altura = input("Erro. Digite novamente. Coloque um numero real: ")
   
    try:
        altura = float(altura)
    except ValueError:
        altura = input("Erro. Digite novamente. Coloque um numero real: ")

    # equação e print
    pesoIdeal = (72.7*float(altura)) - 58
    print("O peso ideal é: " + str(pesoIdeal))

pesoIdeal()


# Questão 13
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
def pesoIdealHeM():
    # coleta de dado
    altura = input("digite sua altura: ")

    # tratamento de erros
    for digito in altura:
        if digito == "-":
            altura = input("Erro. Digite sua altura: ")
   
    try:
        altura = float(altura)
    except ValueError:
        altura = input("Erro. Digite novamente. Coloque um numero real: ")

    # coleta de dado e tratamento de erro
    genero = input("digite m para mulher e h para homem: ")
    if genero != "m" and genero != "h":
        genero = input("Erro. Digite novamente. Coloque h para homem ou m para mulher: ")

    # aplicacao de formula conforme genero
    if genero == "h":
        pesoIdeal = (72.7*float(altura)) - 58
    else:
        pesoIdeal = (62.1*float(altura)) - 44.7
    print("O peso ideal é: " + str(pesoIdeal))

pesoIdealHeM()


# Questão 14
'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João 
deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''
def pesoPeixes():
    # coleta o peso dos peixes e converte para float
    pesoPeixes = input("digite quantidade em kg de peixes coletados: ")    

    # Tratamento de erros
    for digito in pesoPeixes:
        if digito == "-":
            pesoPeixes = input("Erro. Digite quantidade em kg de peixes coletados: ")
   
    try:
        pesoPeixes = float(pesoPeixes)    
    except ValueError:
            pesoPeixes = input("Erro. Digite novamente. Digite quantidade em kg de peixes coletados: ")
    
    # calcula excedentes e multa
    if float(pesoPeixes) > 50.0:
        excedente = pesoPeixes - 50.0
        excedente = round(excedente+0.5)
        multa = 4*excedente
    else:
        excedente = 0
        multa = 0

    # prints
    print("Quantidade de kg excedentes: " + str(excedente))
    print("Multa a ser paga: " + str(multa))

pesoPeixes()