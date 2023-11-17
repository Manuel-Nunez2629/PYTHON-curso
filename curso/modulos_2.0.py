#si el modulo estuviera dentro de una carpeta en la misma ruta osea dentro de este archivo 
#import funciones_buenas.saludar 

#print(funciones_buenas.saludar.saludar('Manuel')) 

#fuera o al mismo nivel jerargico
import sys 
#agregamos la ruta del archivo
sys.path.append('D:\\python_curso\\funciones_buenas')
#podemos ver dodne esta el archivo fuente y por ultimo el archivo que agregamos
print(sys.path)

import saludar as saludito
print(saludito.saludar('Manuelito'))