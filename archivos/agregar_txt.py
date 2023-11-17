with open('texto_nanu.txt','a',encoding = 'UTF-8') as archivo:
#con el permiso de "a" append agrega el write solamente
    #sobreescribimos el archivo
    archivo.write('\n')
    for i in range(5):
        archivo.write(f'Linea {i+1} Agregada\n')



