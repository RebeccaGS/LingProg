''' Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo . 2A vezes B/2
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''


def pedirNumero():
    
    coletarPrimeiroInt = input("Coloque um numero inteiro: ")
    primeiroInt = int(coletarPrimeiroInt)
    coletarSegundoInt = input("Coloque outro numero inteiro: ")
    segundoInt = int(coletarSegundoInt)
    numReal = input("Coloque um numero real: ")

    print(type(primeiroInt))
    produtoDobro1Metade2 = primeiroInt*2*segundoInt%2
    print("produto do dobro do primeiro com metade do segundo: ")
    print(produtoDobro1Metade2)


pedirNumero()