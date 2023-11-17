#creando una funcion que nos devuelva los numeros primos entre el 0 y el argumento que nos pasara
#verifica si son primos
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre 2 y ese mismo -1
    for i in range(2,num-1):
        #si es divisibble por alguno retornamos false y termina el bucle
        if num%i==0: 
            return False
    #si termina el buvle significa que no fue divisible entonces es primo
    return True
#creando funcion que retorna una lista con todos los primos en un rango de 3 hasta el numero ingresado
def primos_hasta (num):
    #creamos una lista donde guardaremos los numeros primos
    primos = []
    #todos los primos en un rango de 3 hasta el numero ingresado
    for i in range(3,num+1):
        #verificamos si el valor es primo con la funcion anterior
        resultado = es_primo(i)
        #si es primo nos devuelve true y lo anadimos a la lista
        if resultado == True: primos.append(i)
    #devolvemos el valor a la lista
    return primos

#creamos el resultado llamando la funcion y lo mostramos en un print
resultado = primos_hasta(98)
print(resultado)


#codigo DAlto
'''primos_hasta = lambda num: list(filter(lambda x: all(x%i != 0 for i in range(2, int(x** 0.5) + 1)), range(2,num)))
print(primos_hasta(15))

lambda num:: Define una función anónima (lambda) que toma un parámetro num.

range(2, num): Genera una secuencia de números desde 2 hasta num - 1.

lambda x: all(x%i != 0 for i in range(2, int(x**0.5) + 1)): Define otra función lambda 
que toma un número x y verifica si x es primo utilizando una expresión generadora y la 
función all.

x % i != 0 for i in range(2, int(x**0.5) + 1): Genera una secuencia de booleanos que 
evalúa si x no es divisible por ningún número en el rango de 2 hasta la raíz cuadrada 
de x (se utiliza int(x**0.5) + 1 para asegurarse de que se incluya la raíz cuadrada si 
es un número entero).

all(...): Devuelve True si todos los elementos de la secuencia son True, es decir, 
si x no es divisible por ningún número en el rango, entonces all(...) devuelve True.

filter(...): Filtra los números en el rango (2 hasta num - 1) que cumplen la 
condición dada por la función lambda. En este caso, filtra los números primos.

list(...): Convierte el objeto filtrado a una lista.

print(primos_hasta(15)): Imprime la lista de números primos hasta el número 15.'''