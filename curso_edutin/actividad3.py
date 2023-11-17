'''Imagina que culminaste el 5º semestre de la universidad, en el cual viste las siguientes 
asignaturas: Seguridad Informática, Ingeniería Web, Inteligencia Artificial, Programación Móvil y Redes;
y las notas fueron las siguientes: 5.0, 4.5, 3.6, 3.9 y 4.3 respectivamente. 
Teniendo claro esto, escribe un programa que solicite tu nombre completo, 
el nombre de las cinco materias y la calificación de cada una. Y como resultado 
devuelve tu nombre y el promedio obtenido en el semestre.'''

print("\nBienvendio a la Calculadora de Promedios UTP\n")
nombre = input("Ingrese su Nombre Completo\n")
nota1 = 0

for i in range(5):
    
    asignatura = input("Nombre de la Asignatura: ")
    nota = float(input("Ingrese su Nota final de la asignatura: "))
    nota1 = nota1+nota

promedio = round(nota1/5,1) 
print(f'Hola {nombre}\nTu promedio este semestre es: {promedio}')

'''Bienvendio a la Calculadora de Promedios UTP

Ingrese su Nombre Completo
Manuel Nunez
Nombre de la Asignatura: seguridad informatica
Ingrese su Nota final de la asignatura: 5.0
Nombre de la Asignatura: ingenieria web
Ingrese su Nota final de la asignatura: 4.5
Nombre de la Asignatura: inteligencia artificial
Ingrese su Nota final de la asignatura: 3.6
Nombre de la Asignatura: programacion movil
Ingrese su Nota final de la asignatura: 3.9
Nombre de la Asignatura: redes
Ingrese su Nota final de la asignatura: 4.3
Hola Manuel Nunez
Tu promedio este semestre es: 4.3'''
#Codigo mejorado
#pedimos los datos personales al usuario
print('Bienvenidos al Sistema de Notas')
nombre=input('Ingresa tu nombre: ')
apellido=input('Ingresa tu apellido: ')
curso=input('Ingreesa tu curso: ')
#creamos las listas
materias=[]
notas =[]
suma_total=0
print('A continuacion ingresaras tus materias y notas respectivamente\n')

#funcion para mostrar todos los resultados 
def final(resultado):
    print(f'Hola {nombre} {apellido} del curso {curso}\nTus notas este semestre fueron: ')
    for materia,nota in zip(materias,notas):
        print(f'Sus materias y sus notas fueron:')
        print(f'{materia}: {nota}')
    print(f'Tu promedio total por semestre fue: {round(resultado,1)}')

#pediremos los datos en un rango  de 5 para que el ciclo cumpla y cuando termine entonces se mueva al otro metodo

def datos(suma_total):
    #declaro la variable resultado como global para poder utilizarla en otro metodo
    global resultado
    #creo un for en un rango de 5 para pedir el nombre y nota
    for i in range(5):
        materia=input('Ingresa el Nombre de la Asignatura\n')
        nota= float(input('Ingresa la nota de la Asignatura\n'))
        #agrego a las listas los datos ingresados en nota y materia
        materias.append(materia)
        notas.append(nota)
        #sumo los valores ingresados en nota en la variable suma total
        suma_total += nota
        #hago la formula para el promedio sumando todos los valores en (suma total)y dividiendolos entre la cantidad de notas
        resultado = suma_total/5
    else:
          final(resultado)

datos(suma_total)








