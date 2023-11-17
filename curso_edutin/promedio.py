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