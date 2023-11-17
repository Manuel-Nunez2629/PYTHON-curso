#creando una lista con frutas
frutas = ['melon','banana','pera','ciruela','manzana','naranja','mandarina']
cadenas = 'Hola Manuel'
numeros = [2,5,8,10]
#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'me voy a comer {fruta}')

#evitar que el bucle siga ejecutandose cuando llega a la fruta seleccionada entonces se termina y sale 
# del bucle(el else no se ejecuta cuando esta el break)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
print(f'Se termino el bucle')

#recorrer una cadena de texto
for letra in cadenas:
    print(letra)


#como duplicar una lista en otra
'''numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)
'''
#for en una linea de codigos
numeros_duplicados= [x/2 for x in numeros];print(numeros_duplicados)
