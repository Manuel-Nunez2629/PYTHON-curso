def obtener_calificaciones():
    calificaciones = [] 
    for i in range(10):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación de la asignatura {i+1}: "))
                if 0 <= calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return calificaciones

def main():
    print("Ingrese las calificaciones del alumno:")
    calificaciones = obtener_calificaciones()

    print(f"\nEl promedio del alumno es: {sum(calificaciones) / len(calificaciones):.2f}")
    print(f"La mejor calificación del alumno es: { max(calificaciones)}")
    print(f"La peor calificación del alumno es: {min(calificaciones)}")
    print(calificaciones)
if __name__ == "__main__":
    main()