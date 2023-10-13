'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

class TV:

    # iniciando atributos
    def __init__(self,channel,volume):
        self.channel = channel # entre 0 e 150, verificar se é int 
        self.volume = volume # entre 0 e 100, verificar se é int

    def changeChannel(self, channel):
        while True:
            try: # tenta transformar em int, se tiver letra, vai pra except, pede outro canal valido
                self.channel = int(channel)
                if self.channel < 150 and self.channel > 0: # ve se ta dentro do escopo de canais validos
                    break # ou poderia pedir pra return True
                else:
                    number = input("Error. Digit again. Put a valid Channel in between 0 to 150: ")
                    channel = number

            except:
                number = input("Error. Digit again. Put a valid Channel in between 0 to 150: ")
                channel = number

    def changeVolume(self, volume):
        while True:
            try:
                self.volume = int(volume)
                if self.volume < 100 and self.volume > 0:
                    break # ou poderia pedir pra return True
                else:
                    number = input("Error. Digit again. Put a valid volume in between 0 to 100: ")
                    volume = number

            except:
                number = input("Error. Digit again. Put a valid volume in between 0 to 100: ")
                volume = number
        
    def returnChannelVolume(self):
        return f'The channel is {self.channel} and the volume is {self.volume}'

# create the object
infos = TV(1,0)


# send to the class 
#infos.changeChannel('a')
#infos.changeVolume('b')
#infos.changeVolume(150)
#infos.changeChannel(-2)

# Print the values
print(infos.returnChannelVolume())


    