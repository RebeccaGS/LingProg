"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa
pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class People:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = int(age)
        self.weight = float(weight)
        self.height = float(height)
    
    # mais velho
    def gettingOlder(self, olderAge):
        self.age = self.age+int(olderAge)
        if self.age < 21:
            self.height = 0.05*self.height
            return self.height
        else:
            self.height = 20*0.05
            return self.height
        
    # engordar
    def gettingFatter(self,overWeight):
        self.weight = self.weight+float(overWeight)

    # emagrecer
    def gettingSlimmer(self, lessWeight):
        self.weight = self.weight-float(lessWeight)

rebecca = People('Rebecca', 20, 60, 1.68)
rebecca.gettingFatter(5) # engordar 5 kg
rebecca.gettingOlder(4) # ficar 4 anos mais velha, printar 24 anos
rebecca.gettingSlimmer(3) # perder 3kg, printar 62kg
print(f'{rebecca.name} has {rebecca.age} years old, {rebecca.weight} kg and {rebecca.height} m.')

