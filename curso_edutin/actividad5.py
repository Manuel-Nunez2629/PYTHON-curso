agenda = {"Jose": 302944, "Mario": 829455, "Angel": 829405,"Luis": 930594}

consultaando = True

while consultaando: 
    print()
    print("Bienvenido a la Agenda telefonica")
    print("Que desea Hacer\n(1).Consultar\n(2).Anadir\n(3).Modificar\n(4).Borrar\n(5).Salir\n")
    opcion =  ""

    while opcion not in ("1","2","3","4","5"):
        opcion = input("--> ")
        if opcion == "1":
            nombre = input("Nombre: ")
            if nombre not in agenda:
               print("este nombre no se encuentra en la agenda")
            else:
                telefono = agenda[nombre]
                print(nombre, ":", telefono)
        elif opcion == "2":
            nombre = input("Nombre:  ")
            if nombre in agenda:
                print("Este nombre ya se encuentra registrado en la Agenda")
            else:
                telefono = int(input("Ingrese el telefono: "))
                agenda[nombre] = telefono
                print("El Telefono se ha agregado correctamente")
        elif opcion == "3":
            nombre = input("Nombre: ")
            if nombre not in agenda:
                print("Nombre no encontrado en la Agenda")
            else:
                telefono = agenda[nombre]
                print("Se ha Modificado el numero")
        elif opcion == "4":
            nombre = input("Nombre: ")
            if nombre not in agenda:
                print("No existe ese nombre en la Agenda ")
            else:
                del agenda[nombre]
                print("Se ha borrado exitosamente")
        elif opcion == "5":
            consultaando = False
            print("Gracias por utilizar Nuestra Agenda :)")
           

