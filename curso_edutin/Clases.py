class Bicicleta:
    def __init__(self,color,cambios,rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin 
        

    def frenar(self):
        return "La bicicleta esta frenada."

    def avanzar(self):
        return "La bicicleta esta en movimiento."
    
    def girar(self):
        return "La bicicleta esta girando."
    
urbana = Bicicleta("rojo",8,27.5)
hibrida = Bicicleta("azul", 1,29)

print ("Urbana: "+str(urbana.color))

print("Comportamiento de la bicicleta urbana: "+ str(urbana.girar()))
print("\n")
print ("Hibrida: "+str(hibrida.color))

print("Comportamiento de la bicicleta urbana: "+ str(urbana.avanzar()))