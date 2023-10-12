# Mudar valor do Lado, Retornar valor do Lado e calcular Área;

# criando classe quadrado
class Square:
    def __init__(self,side): # atributo side = tamanho
        self.side = side
    
    def changeSide(self, side): # metodo: mudar valor do lado
        self.side = side

    def returnValueSide(self):
        return f"the side of square is {self.side} cm" # define o return da classe
    
    def calculateArea(self):
        self.side = float(self.side)
        area = self.side*self.side
        return f"the area is {area} cm^2"

# Criando Objeto
square1 = Square(5)

# Pede novo lado ao usuario
newSide = input("Whats the side about the square 1? Put in cm please: ") # pede ao usuario tamanho do lado do quadrado

# Envia o novo tamanho pra func mudar lado
square1.changeSide(newSide)

# Printar valor do lado e sua área
print(square1.returnValueSide())
print(square1.calculateArea())