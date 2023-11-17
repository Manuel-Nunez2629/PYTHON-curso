#forma no optima de sumar valroes
'''def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados+numero
    return numeros_sumados

resultado = suma([5,3,9,10,20,3])'''
#forma optima de sumar valroes
'''def suma(*numeros):
    return sum(numeros)'''
#utilizando el operador * como argumento args
def suma (nombre, *numeros):  
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

#Manuel, la suma de tus numeros es: 50


#forma optima con la funcion args
def suma_total(numeros):
    return sum([*numeros])

resultado = suma_total([5,3,9,10,20,3])
print(resultado)
