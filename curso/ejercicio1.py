#duracion de cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#crudo de video vacio
crudo_promedio = 5
crudo_dalto = 3.5
#sacando el procentaje de cursos
tiempo_vacio_promedio = round(100 - otros_cursos_promedio/crudo_promedio *100,1)
tiempo_vacio_dalto = round(100 - dalto_curso/crudo_dalto *100,1)
#diferencias de duraciones entre otros
diferencia_min = 100 - dalto_curso/otros_cursos_min *100
#se utiliza la division baja para redondear mas el numero y ademas lo multiplicamos por mil para agregarle mas ceros y despues quitamos los excedentes dividiendolo entre 10
'''diferencia_max = 100 - dalto_curso*1000//otros_cursos_max /10'''
diferencia_max = round(100 - dalto_curso/otros_cursos_max *100,1)
diferencia_promedio = round(100 - dalto_curso/otros_cursos_promedio *100,1)

print(f'Este curso dura un {diferencia_min}% menos que el curso mas rapido')
print(f'Este curso dura un {diferencia_max}% menos que el curso mas rapido')
print(f'Este curso dura un {diferencia_promedio}% menos que el curso mas rapido')
print('------------------------------------------------------------------------')

print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de video vacio')
print(f'este curso elimina un {tiempo_vacio_dalto}% de video vacio')
print('------------------------------------------------------------------------')

print(f'Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio/dalto_curso*10,1)} horas de otros cursos')
print(f'Ver 10 horas otros cursos equivale a ver {round(dalto_curso/otros_cursos_promedio*10,1)} horas de este curso')
print('------------------------------------------------------------------------')