#creabdi fybcuib qye suma numeros
def sumar_dos():
    while True:
        #pidiendo los datos
        a=input('Numero1: ')
        b = input('Numero 2: ')
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a)+int(b)
            #si lanzo una excepcion pedirle que reingrese los datos
        except Exception as e:
            print('Te pedi un numero salame, no te hagas el gracioso')
            print(f'Error: {e}')
        #si todo sale bien terminamos el bucle
        else:
            break
        finally:
            print('Se ejecuta siempre , Manejo de excepcion finalizado')
    #retornando el resultado
    return resultado

print(sumar_dos())
