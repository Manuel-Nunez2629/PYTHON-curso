#hoy falto el profesor de clase y se ordenaron para hacer la suya propia
#(A) pedir la edad de los companieros que vinieron hoy a clase y ordenar los datos de menor a mayor
#(B)El mayor es el profesor y el menor es el asistente: Quien es quien
#recibimos un dato numero para saber cuantas veces se repetira el bucle for
num_estudiantes= int(input("cuantos estudiantes son: "))
#creamos la lista que contendra a todos los compañeros
estudiantes=[]
#utilizamos un for para poder ir ingresando los nombre y edades de los estudiantes
for i in range(num_estudiantes):
    #pedimos nombre y edad
    estudiante=(input("Ingresa tu nombre: "))
    edad=int(input("ingresa tu edad: "))
    #guardamos la informacion en tuplas
    compa = (estudiante,edad)
    #agregamos la informacion a la lista
    estudiantes.append(compa)
    #ordenando de menor a mayor segun su edad
    estudiantes.sort(key=lambda x:x[1])
    #estudiantes [x] devuelve una tupla con nombre y edad y depues accedemos al nombre 
    asistente = estudiantes[0][0]
    profesor = estudiantes[-1][0]
   
print(f'el asistente es: {asistente} y el profesor es: {profesor}')
        

       

