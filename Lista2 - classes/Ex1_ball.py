# classe ball
class Ball:
    ## __init__: sempre executada quando classe inicia
    def __init__(self, color, material, circumference): # coloca atributos
        self.color = color
        self.material = material
        self.circumference = circumference

    ## __str__: seta o que deve ser retornado da classe - não pediu, só pra guiar
    def __str__(self):
        return f"the ball is {self.color}, made of {self.material} and has a circumference of {self.circumference} cm. "

    ## Metodos: funçoes dentro de classe
    def trocaDeCor(self, color):
        self.color = color

    def mostraCor(self):
        return f"The color of the ball is: {self.color}"

## Objeto bola
ball1 = Ball('blue', 'rubber', 3.14)

# printa só o objeto cor
print(ball1.mostraCor())

# printa o que foi definido na função __str__
print(ball1)

# pede nova cor ao usuario
newColor = input("Whats the new color of the ball? ")

# muda a cor no objeto ball1
ball1.trocaDeCor(newColor)

# printa texto com nova cor
print(ball1.mostraCor())

