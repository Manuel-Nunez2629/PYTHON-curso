class Gato():
    def sonido(self):
        print("Miau")

class Perro():
    def sonido(self):
        print("Guau")

class Cerdo():
    def sonido(self):
        print("OINK OINK")


def escucharsonido(animal):
    animal.sonido()
'''def escucharsonido(animal/el elegido):
    //el elegido/animal.sonido()'''
gato1 = Gato()

perro1 = Perro()

cerdo1 = Cerdo()
escucharsonido(cerdo1)
        