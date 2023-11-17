class Persona():
    def __init__(self,identificacion,edad,nombre):
        self.__identificacion = identificacion
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return 'Hola'+self.nombre
    #otra forma de obtener la informacion si esta privada con get
    def getidentificacion(self):
        return self.__identificacion
    
    def setidentificacion(self,valor):
        self.__identificacion = valor  
        
    
Persona1= Persona(8954,25,'Manuel')

print(Persona1.getidentificacion())
Persona1.setidentificacion(55646498)
print(Persona1.edad)
#para asignar un valor a algo con un Set
print(Persona1._Persona__identificacion)
print(Persona1.nombre)

