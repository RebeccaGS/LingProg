
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
    primeiroInt = int(primeiroInt)
    
    segundoInt = input("Coloque outro numero inteiro: ")
    segundoInt = int(segundoInt)
    
    numReal = input("Coloque um numero real: ")
    numReal = float(numReal)

    # equacoes
    produtoDobro1Metade2 = primeiroInt*2*segundoInt/2
    somaTriplo12 = primeiroInt*3 + numReal
    terceiroCubo = numReal*numReal*numReal

    # prints
    print("Produto do dobro do primeiro com metade do segundo: " + str(produtoDobro1Metade2))
    print("A soma do triplo do primeiro com o terceiro: " + str(somaTriplo12))
    print("O terceiro elevado ao cubo: " + str(terceiroCubo))


# Questão 12
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def pesoIdeal():
    altura = input("digite sua altura: ")
    altura = float(altura)
    pesoIdeal = (72.7*altura) - 58
    print("O peso ideal é: " + str(pesoIdeal))


# Questão 13
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
