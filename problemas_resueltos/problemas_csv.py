import pandas as pd

df = pd.read_csv('\\python_curso\\archivos\\datos.csv')
#convertir a string los datos de una columna 
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(df['edad'][0])

#remplazando los datos Nuñez por Papucho
df['apellido'].replace('nuñez','Papucho',inplace=True)

#print(df['apellido'])
#eliminando filas con datos faltantes
df=df.dropna()
#eliminando filas con repetidos
df=df.drop_duplicates()


#creando un csv con el datafgrame resultante(limpio)
#rutas solamente asi
df.to_csv('\\python_curso\\problemas_resueltos\\datos_limpios.csv')
