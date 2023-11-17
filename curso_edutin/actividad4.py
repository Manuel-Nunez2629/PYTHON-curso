'''La función principal tendrá como parámetros: 
nombre de la moneda actual
valor de la monedad actual 
y nombre de la moneda a comvertir

'''


print("Hola\n Bienvenido al conversor de monedas")


def pregunta(monedaactual):
    
    if monedaactual == 1:
        
        eledolar(monedaaconvertir,valor)

    elif monedaactual == 2:
        eleeuro(monedaaconvertir,valor)
    else:
        print("Ingrese nuevamente un valor aceptable\n")
        pregunta()

def eledolar(monedaaconvertir,valor):
    def dolar():
            print("Has elegido la conversion de \n DOLAR")
            if monedaaconvertir == 1:
                resultado = round(valor*3750,2)
                print(f'{valor} dolares es igual a {resultado} pesos colombianos')
                regreso = input("Desea volver a realizar otra conversion\n:")
                if regreso == 1:
                    pregunta(monedaactual)
                else:
                    print("Gracias Por haber utilizado el conversor")

            elif monedaaconvertir == 2:
                resultado = round(valor*6.37,2)
                print(f'{valor} dolares es igual a {resultado} Yuanes')
              
            elif monedaaconvertir == 3:
                resultado = round(valor*0.76,2)
                print(f'{valor} dolares es igual a {resultado} Libras esterlinas')
                
            else:
                print("Ingrese nuevamente un valor aceptable\n")
    dolar()

def eleeuro(monedaaconvertir,valor):
    def euro():
            print("Has elegido la conversion de \n EURO")
            if monedaaconvertir == 1:
                resultado = round(valor*4000,2)
                print(f'{valor} Euros es igual a {resultado} pesos colombianos')

            elif monedaaconvertir == 2:
                resultado = round(valor*6.93,2)
                print(f'{valor} Euros es igual a {resultado} Yuanes')
            elif monedaaconvertir == 3:
                resultado = round(valor*0.83,2)
                print(f'{valor} Euros es igual a {resultado} Libras esterlinas')
            else:
                print("Ingrese nuevamente un valor aceptable\n")
    euro()  


monedaactual = int(input("que tipo de conversor deseas utilizar:\n Ingresa 1 para dolar \n ingresa 2 para Euro\n"))
valor = float(input("Ingresa la Cantidad a Convertir:\n"))
monedaaconvertir = int(input("ingrese la Moneda a Convertir\n 1.Pesos colombianos\n2.Yuanes\n3.Libras esterlinas\n"))
pregunta(monedaactual)



'''
Hola
 Bienvenido al conversor de monedas
que tipo de conversor deseas utilizar:
 Ingresa 1 para dolar
 ingresa 2 para Euro
1
Ingresa la Cantidad a Convertir:
50
ingrese la Moneda a Convertir
 1.Pesos colombianos
2.Yuanes
3.Libras esterlinas
1
Has elegido la conversion de 
 DOLAR
50.0 dolares es igual a 187500.0 pesos colombianos

Hola
 Bienvenido al conversor de monedas
que tipo de conversor deseas utilizar:
 Ingresa 1 para dolar
 ingresa 2 para Euro
2
Ingresa la Cantidad a Convertir:
30
ingrese la Moneda a Convertir
 1.Pesos colombianos
2.Yuanes
3.Libras esterlinas
2
Has elegido la conversion de 
 EURO
30.0 Euros es igual a 207.9 Yuanes

Hola
Bienvenido al conversor de monedas
que tipo de conversor deseas utilizar:
 Ingresa 1 para dolar
 ingresa 2 para Euro
2
Ingresa la Cantidad a Convertir:
15
ingrese la Moneda a Convertir
1.Pesos colombianos
2.Yuanes
3.Libras esterlinas
3
Has elegido la conversion de 
 EURO
15.0 Euros es igual a 12.4 Libras esterlinas'''