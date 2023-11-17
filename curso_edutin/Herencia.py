class Vehiculo:
    def __init__(self,matricula,modelo,marca,color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False


    def avanzar(self):
        self.avanza = True

    def frenar(self):
        self.frena = True

    def girar(self):
        self.gira = True

    def imprimir (self):
        print(f'Matricula: {self.matricula}\nModelo: {self.modelo}\nMarca: {self.marca}\n'
              f'Color: {self.color}\nAvanzar: {self.avanza}\nFrenar: {self.frena}\nGirar: {self.gira}\n')
#Clase hija para usar argumentos en la nueva tenemos que usar el super para heredar los metodos con esos atributos.       
class Moto(Vehiculo):
    def __init__(self, matricula, modelo, marca, color,cilindraje):
        super().__init__(matricula, modelo, marca, color)

        self.cilindraje = cilindraje
        

moto1=Moto("ABC123",2018,"BMW","Rojo",150)
moto1.avanzar()
moto1.girar()
moto1.frenar()
print(f'Cilindraje: {moto1.cilindraje}')
moto1.imprimir()
        


        