'''
en una escuela de conduccion tiene un programa que dependiendo de 
la edad del usuario debe mostrar el tipo de licencia a al que tiene derecho
condicion 1 si es menor a 16 no puede conducir
condicion 2 si es menor a 18 puede obtener el permiso para conducir
condicion 3 si es menor a 70 puede obtener una licencia estandar
condicion 4 si es mayor a 70 entonces necesita una licencia especial
'''
print("Bienvenido")
print("Introduzca su edad para mostrar tu tipo de licencia")
edad = int(input(": "))

if edad < 16:
    print("es menor a 16 no puede conducir")
elif edad < 18 :
    print("es menor a 18 puede obtener el permiso para conducir")
elif edad < 69:
    print("Puede obtar por una licencia Estandar")
else:
    print("usted es mayor a 70, necesita una licencia especial")


print("Pase a verificar sus datos.")
