
def es_par(numero):
    if numero % 2 == 0:
        print("el numero es par "+str(numero))
    else:
        print("el numero es impar "+str(numero))


def saludar(nombre):
    print(f'hola {nombre} eres el mejor programador')


def resta(a = None, b = None):
    if a == None or b == None:
        print("debes ingresar 2 numeros")
        return
    return a-b

resultado = resta(1,4)



def multiplicacion(numero = None):
    if numero == None:
        print("introduzca un numero")
    else:
        for i in range(0,13):
            print(f'{numero} X {i} = {i * numero}')

saludar("manuel")
es_par(6)           
multiplicacion(12)
print(resultado)