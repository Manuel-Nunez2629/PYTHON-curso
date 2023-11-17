
contrasenia = input("Ingresa una contrasenia: ")

edad = int(input("Introduzca su edad: "))
graduacion = input("Te has graduado?: ")

if (len(contrasenia) >= 8):
    print("La contrasenia es lo suficiente mente larga")
    if contrasenia == 'prueba123':
        print("La contrasenia es correcta")
    else:
        print("La contrasenia es incorrecta")
else:
    print("La contrasenia es muy corta e insegura")


if edad >18 :
    print("felicidades ya tienes la mayoria de edad")
    if graduacion == 'si':
        print("felicidades por tu graduacion")
    elif graduacion == 'no':
        print("hechale ganas pues")
else:
    print("aun eres menor de edad")
    if graduacion == 'si':
        print("Felicidades por tu graduacion")
    elif graduacion == 'no':
        print("hechale ganas pues")




