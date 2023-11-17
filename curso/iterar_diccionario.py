diccionario = {
    'nombre':'manuel',
    'apellido':'nunez',
    'numero':658684
}
#nos muestra la clave solamente la clave
#para mostrar los elementos agregamos el metodo items()
'''for key in diccionario:
    print(key)'''
#con esto obtenemos las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es {key} y el valor es {value}')