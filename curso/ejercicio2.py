palabra = input('Ingrese un texto: \n')
#el usuario ingresa un texto de cualquier manera
frase = palabra.split(" ")
#utilizamos el metodo split para separar las cadenas en frases a partir del espacio
#contamos la cantidad de palabras separadas por el espacio
cantidad_de_palabras = len(frase)
# si es mayorr a 120 entonces entra en el if
if cantidad_de_palabras >= 120:
    print("Para tampoco era escribir un estamento")

print(f'Usted dijo : {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos')
print(f'Dalto lo diria en {round(cantidad_de_palabras/2/1.30,1)} segundos' )

