print("\nBienvendio a la Calculadora de Promedios UTP\n")

nota = 0

asignatura = [25]
nota = [5]

def datos():
    nombre = input("Ingrese su nombre completo\n")
   


def estudiante():
    contador = 0
    nota1= 0
    for i in range(5):
            contador += 1
            asignatura[i] = str(input("Nombre de la Asignatura: "))
            nota[i] = float(input("Ingrese su Nota final de la asignatura: "))
            nota1 = nota1+nota[i]
            
    promedio = round(nota1/5,1) 
   
    


def muestra():
    for i in range(5):     
        print("nota: " + i + ": "+ nota[i])    
  

datos()
estudiante()
muestra()
    


'''    
print(f'Hola {nombre}\nTu promedio este semestre es: {promedio}')    
    

for clave in lenguajes:
        contador +=1
        print(f'tu {contador} lenguaje favorito es: {lenguajes[clave]}')
'''


