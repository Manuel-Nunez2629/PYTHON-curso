#registrar esta informacion en un txt de forma optima
with open('pedos.txt','w') as archivo:
    numero,numero2=1,3
    for i in range(0,16):
        archivo.writelines(f'01-{numero},{numero2}\n')
        numero =numero +1
        numero2 = numero2+3
        