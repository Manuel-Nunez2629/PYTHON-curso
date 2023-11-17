#creamos una lista llamada animales
animales = ['pez','loro','perro','jaguar','gato','zeus','sardina']
#creamos una lista de numeros
numeros = [65,45,21,9,8,778,574]
#con esto ordenamos la lista de menor a mayor
resultado = numeros.sort()

'''#Tabla de multiplicar
numtabla = int(input("Desea el numero de la tabla de multiplicar: "))
print("")

print(f'La tabla de multiplicar eslegida fue la del {numtabla}')
 
for i in range(0,13):
    print(f'{numtabla} X {i} = {i * numtabla}')'''

#creamos un for para que recorra los numeros de la lista numeros  y multiplique cada dato*10
for multiplo in numeros:
    resultado = multiplo*10
    print(f'el multiplo de {multiplo} = {resultado}')

#recorre la lista de animales
for animal in animales:
    print(animal)

#agrupamos dos lists tienen que ser de el mismo tamanio de datos for dato1,dato2 in zip(lista1,lista2):
for animal,numero in zip(animales,numeros):
    print(f'recorriendo lista 1: {animal},{numero}')
    print(f'recorriendo lista 2: ')

#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])


#forma correcta de recorrer una lista obteniendo el indice de la lista
#La función enumerate permite asociar un contador como clave a cada elemento del conjunto, lo que facilita su estructuración. 
#Al enumerar el conjunto, podemos controlar mejor y de manera más confiable la forma como interactuamos con sus elementos.
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#utilizando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle,valor actual: {numero}')
else:
    print('el bucle temrino')

#todo esto sirve con tuplas tambien
    