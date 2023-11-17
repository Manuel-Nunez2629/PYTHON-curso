
#funcion simple
'''def saludar():
    print(f'Saludos')

#ejecutando funcion simple
saludar()'''

#parametros se creran para usarse en una funcion pero fuera no se utiliza
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == 'hombre':
        print(f'Hola {nombre} Fiera, como andas')
    elif sexo == 'mujer':
        print(f'Hola {nombre} Corazon, como andas')
    else:
         print(f'Hola {nombre} Helicoptero Apache, como andas')

saludar('Manuel','Hombre')
saludar('Virginia','Mujer')
saludar('Tristam','No-Binary')

#crear una funcion que nos retorne valores multiples avalores
def crear_contrasenia_random (num):
    #creamos caracteres aleatorios
    chars = 'abcdefghij'
    #el num de entrada se convierte en cadena de texto
    num_entero = str(num)
    #luego el primer digito de la cadena de texto se convierte nuevamente en un numero entero por 
    # ejemplo si el num es 123 despues de esta linea sera 1
    num = int(num_entero[0])
    #se resta 2 al valor de num y se guarda en c1
    c1 = num - 2
    c2 = num
    #re resta 5 al valor de num y se guarda en c3
    c3 = num - 5
    #La contraseña se forma concatenando caracteres de la cadena chars 
    #usando los índices c1, c2, y c3, y luego añadiendo el doble del valor de num. 
    # La contraseña generada tendrá un total de 4 caracteres.
    contrasenia = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    #esta funcion se esta convirtiendo un valor y retorna la contrasenia
    return contrasenia
    
password = crear_contrasenia_random(1)
frase = f'Tu contrasenia nueva es {password}'
print(frase)

