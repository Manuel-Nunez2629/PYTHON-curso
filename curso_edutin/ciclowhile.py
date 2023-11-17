#calculadora de indice de masa corporal

print("Calculadora de indice de Masa corporal IMC \n")

contador = 0

while contador != 2 :
    contador = int(input("Quieres seguir calculando el IMC 1.SI y 2.No \n"))
    if contador == 1:
        estatura = float(input("ingrese su estatura en metros: "))
        peso = float(input("ingrese su peso en kg: "))
        resultado = round(peso/(estatura ** 2),2) 
        if resultado < 18.5:
            print(f'IMC {resultado} = Bajo de peso')
        elif 18.5< resultado < 24.99:
            print(f'IMC {resultado} = Peso normal')
        elif 25 < resultado < 30:
            print(f'IMC {resultado} = Sobrepeso')
        elif resultado > 30:
            print(f'IMC {resultado} = Obesidad')

    elif contador ==2:
        print(" Hasta Pronto ")
print("Gracias por utilizar la Calculadora de IMC")
        


