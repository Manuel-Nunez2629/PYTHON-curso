#import modulo_saludar
#cambiarle el nombre al modulo
from modulo_saludar import saludar #se puede utilizar solo el nombre de la funcion

#import modulo_saludar as fokiu
#from modulo_saludar import * mala practica modulo se vuelve pesado
#utilizamos el modulo como un metodo
saludo= saludar('Manuel')
#utilizando las funciones como si fueran funciones creadas gracias al otro import
#saludo = saludar('manuel')
print(saludo)
#con esto podemos ver todo lo declarado en el programa 
# print(dir(modulo_saludar))