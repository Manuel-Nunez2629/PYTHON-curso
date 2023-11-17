#2 listas, una con nombre otra con apellidos
nombres = ["Lucas",'Matias', 'Camila',"Pedro","Roberto"]
apellidos = ["Dalto",'Zing', 'Dalto',"Robetix","tarado"]

#registrar esta informacion en un txt de forma optima
with open('nombres_y_apellidos.txt','w') as archivo:

    archivo.writelines("Los datos son:\n\n")
    
    [archivo.writelines(f'Nombre: {n}\nApellido: {a}\n--------------\n')for n,a in zip(nombres,apellidos)]


    

    