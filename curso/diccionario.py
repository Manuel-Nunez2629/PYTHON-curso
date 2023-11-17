#cradno diccionarios con dict()
#no se pueden crear listas ni tuplas ni set ni diccionarios vacios si no utilizamos la funcion de crear
diccionario = dict(nombre='Manuel',apellido='Nunez')

#las listas no pueden ser clasves porque son iterables y usamos frozenset para utilizar
diccionario2 = {frozenset(['manuel','jose]']): 'jajaj'}

#craeando diccionarios con fromkeys() al
diccionario3 = dict.fromkeys('Nombre','Apellido')
#{'N': 'Apellido', 'o': 'Apellido', 'm': 'Apellido', 'b': 'Apellido', 'r': 'Apellido', 'e': 'Apellido'}
diccionario3 = dict.fromkeys(['Nombre','Apellido'])
#{'Nombre': None, 'Apellido': None}
diccionario3 = dict.fromkeys('ABCD')
#{'A': None, 'B': None, 'C': None, 'D': None}
print(diccionario3)
