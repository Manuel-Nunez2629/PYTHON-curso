
def inicio():
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))
    eleccion = input("Ingrese\n1 para Suma\n2 para Resta\n3 para multiplicacion\n4 para Division\n5 para residuo\n6 elevacion al cuadrado de los valores\n7 para salir\n")
    tipo(num1,num2,eleccion)


def tipo(num1,num2,eleccion):
    if eleccion == '1':
        resultado = (num1+num2)
        print(f'La suma de los valores es: {resultado}')
        pregunta()

    elif eleccion == '2':
        resultado = (num1-num2)
        print(f'La resta de los valores es: {resultado}')
        pregunta()

    elif eleccion == '3':
        resultado = (num1*num2)
        print(f'La multiplicacion de los valores es: {resultado}')
        pregunta()

    elif eleccion == '4':
        resultado = (num1/num2)
        print(f'La division de los valores es: {resultado}')
        pregunta()

    elif eleccion == '5':
        resultado = (num1%num2)
        print(f'el residuo de los valores es: {resultado}')
        pregunta()

    elif eleccion == '6':
        cuadrado1 = num1*num1
        cuadrado2 = num2*num2
        print(f'primer valor al cuadrado {cuadrado1}\nsegundo valor al cuadrado {cuadrado2}')
        pregunta()

    elif eleccion == '7':
        print("Gracias por usar nuestra calculadora.")
    else:
        print("ingrese valores dentro de los parametros.")
        inicio()

    

def pregunta():
    
    respuesta = input("Desea volver al (1)Menu o (2)salir: ")
    if respuesta == '1':
        inicio()

    elif respuesta == '2':
        print("Gracias por usar nuestra calculadora.")
    else:
        print("Porfavor elija una opcion")
        pregunta()
        

inicio()