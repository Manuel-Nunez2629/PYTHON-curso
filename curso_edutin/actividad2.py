print("Bienvenido")
print("Porfavor introduzca sus datos y el valor de su compra")
nombre = input("Su nombre es: ")
valor = float(input("el valor de la compra fue: "))

if valor < 79:
    print("Buenos dias "+ nombre)
    print("El valor de su compra fue de: "+ str(valor))
    print("el valor de la compra fue muy bajo para aplicar un descuento")
    print("su costo total es de: "+ str(valor))
elif valor >= 80 and valor < 149:
    print("Buenos dias "+ nombre)
    print("El valor de su compra fue de: "+ str(valor))
    des10 = (valor*0.1)
    print("El valor total con descuento incluido es de: "+ str(valor-des10))

elif valor >=150 and valor <=300:
    print("Buenos dias "+ nombre)
    print("El valor de su compra fue de: "+ str(valor))
    des15 = (valor*0.15)
    print("El valor total con descuento incluido es de: "+ str(valor-des15))

elif valor > 300 and valor < 500:
    print("Buenos dias "+ nombre)
    print("El valor de su compra fue de: "+ str(valor))
    des20 = (valor*0.20)
    print("El valor total con descuento incluido es de: "+ str(valor-des20))

'''
Buenos dias Angel mario Villa Lopez
El valor de su compra fue de: 455.0
El valor total con descuento incluido es de: 364.0

Rosa Diaz
El valor de su compra fue de: 105.0
El valor total con descuento incluido es de: 94.5

Dilan Gonzalez
El valor de su compra fue de: 250.0
El valor total con descuento incluido es de: 212.5

Kelly Daaza
El valor de su compra fue de: 430.0
El valor total con descuento incluido es de: 344.0
'''