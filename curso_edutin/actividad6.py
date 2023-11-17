class Persona():
    def __init__(self):
        self.nombre = input("Ingrese el Nombre: ")
        self.edad = int(input("Ingrese su Edad: "))

    def imprimir(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}')

    
class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.deposito = float(input("Ingrese un Deposito: "))

    def imprimirdeposito(self):
        print(f'Su deposito fue: {self.deposito}')

    def impuestos(self):
        if self.deposito > 4000:
            print("Si debe pagar impuestos.")
        else:
            print("No debe pagar impuesto")

ciudadano1=Ciudadano()
ciudadano1.imprimir()
ciudadano1.imprimirdeposito()
ciudadano1.impuestos()
'''Manuel Chima si debe pagar impuestos
Fayle Garcia no debe pagar impuesto
Lesly Rodriguez si debe pagar imnpuestos
Mario Herrera no debe pagar impuestos'''
''' 
ciudadano1 = Ciudadano("Manuel Chima",25,6700)
ciudadano1.imprimir()
ciudadano1.imprimirdeposito()
ciudadano1.impuestos()
print("\n")
ciudadano2 = Ciudadano("Fayle Garcia",56,3500)
ciudadano2.imprimir()
ciudadano2.imprimirdeposito()
ciudadano2.impuestos()
print("\n")
ciudadano3 = Ciudadano("Lesly Rodriguez",34,9000)
ciudadano3.imprimir()
ciudadano3.imprimirdeposito()
ciudadano3.impuestos()
print("\n")
ciudadano4 = Ciudadano("Mario Herrera",45,2500)
ciudadano4.imprimir()
ciudadano4.imprimirdeposito()
ciudadano4.impuestos()
''' 


