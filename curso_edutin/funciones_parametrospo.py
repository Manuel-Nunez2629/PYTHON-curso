'''
def suma(a,b,c):
    return a+b+c

resultado = suma(3,4,5)
print(resultado)

def suma(*args):
    s = 0
    for arg in args:
        s+= arg
    return s

resultado = suma(10,10,10,25,4,4,3,4,5,4)

print(resultado)'''
'''
def lenguaje(nombre, *lenguajes):
    print(f'hola {nombre}')
    print(f'tus lenguajes favoritos son: {lenguajes}')

lenguaje("manuel","java",'python',"c++")
'''

def idioma(nombre, **lenguajes):
    print(f'hola {nombre}')
    print(f'tus lenguajes favoritos')
    print("cargando informacion \n")
    print("informacion: ")

    contador = 0
    print(type(lenguajes))

    for clave in lenguajes:
        contador +=1
        print(f'tu {contador} lenguaje favorito es: {lenguajes[clave]}')
    
idioma("Manuel",hola = "rugby",lenguaje2 = "python",lenguaje4 = "Ccharty",lenguaje3 = "Java")
