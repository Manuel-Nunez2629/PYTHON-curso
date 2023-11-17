diccionario ={
    'nombre': 'Manuel',
    'apellido': 'Rivera',
    'subs': 102629
}
#devuelve las claves tambien sirve para iterar
clave = diccionario.keys()

#devuelve el valor de una clave si no encuentra me da un none
claves = diccionario.get('nombre')
#elimina todos los elementos
#diccionario.clear()
#pop elimina un elemnto pop() solo sirve para eliminar UN SOLO elemento
#diccionario.pop('subs')
#para iterar el dicionnario
diccionario_iterable = diccionario.items()

print(diccionario_iterable)