'''ciclo for
for i in elemento:
    #instruccion
    print(f'Mensaje',i)
    #i = variable de iteracion
    #elemento = lista, secuencia de numeros'''
'''
palabra = input("ingrese una palabra: ")
numero = int(input("ingrese el numero de repeticiones: "))
if numero <= 0:
    print("numero de veces muy baja para iterar")
elif numero <= 5:
    print("se mostrara repetida la palabra "+str(numero)+" veces")
    for i in range(numero):
        print(palabra)
else:
    print("fokiu no quiero repetir")


print(f'Hola Bienvenido')
contador = 1

for v in [3,4,5,9,4,1]:
    print(f'vuelta numero {contador}')
    print(f'el cuadrado de {v} es iugal a: {v ** 2}')
    contador += 1
print("final de iteracion")
'''
numtabla = int(input("Desea el numero de la tabla de multiplicar: "))
print("")

print(f'La tabla de multiplicar eslegida fue la del {numtabla}')
 
for i in range(0,13):
    print(f'{numtabla} X {i} = {i * numtabla}')
