'''
crear un programa que reciba el numero de anios que tiene la computadora
imprimir en consola si es nuevo o es viejo
condiciones:
si es menor o igual a 2 anios entonces es nuevo, pero si es mayore a dos anios es viejo
'''
edad = int(input("Introduzca su edad: "))
anios = int(input("Cuantos anios tiene tu computador: "))

if anios    >= 0 and anios <= 2:
    if edad >= 18 :
        print("usted es mayor de edad")
        print("tu computadora es nueva")
    else: 
        print("usted es menor de edad")
        print("tu computadora es nueva")
else:
    if edad >= 18 :
        print("usted es mayor de edad")
        print("tu computador es viejo")
    else: 
        print("usted es menor de edad")
        print("tu computador es viejo")

print("Hasta la proxima")


