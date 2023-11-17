'''Crear una tupla con numeros luegoi pedir un numero por teclado e indicar cuantas veces se repite'''

numeros = (5,6,7,8,5,5,6,90,12,14,12)

numero = int(input("Dame un numero: "))

print("El numero se repite: "+ str(numeros.count(numero)) + " veces")

print("El numero "+ str(numero) + " se encuentra en el indice:" + str(numeros.index(numero)))
