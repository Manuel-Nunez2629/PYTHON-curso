#se utiliza para ahorrarnos todo el codigo un bloque de una funcion se puede utilizar lambada
#creando una funcion lambda para multiplicar
# no son aptas para cuando damos mas de una expresion no funciona
multiplicar_por_dos = lambda x:x*2

#rint( multiplicar_por_dos(2))

#usando filter con una funcion comun
numero=[1,2,3,4,5,6,7,8,9]
def es_par(num):
    if num % 2 == 0:
        return True
#nos ingresa los datos true en esta lista filter y se la pedimos conviritendo la variable en list()
numeros_par = filter(es_par,numero)
print(list(numeros_par))

#creando la funcion con lambda
numeros_pares = filter(lambda numero:numero%2==0,numero)
print(list(numeros_pares))
