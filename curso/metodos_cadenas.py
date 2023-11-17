cadena1 = 'Hola soy Manuel'
cadena2 = 'alfanumericonumero'
#Convierten valores
#convierte a mayusculas
resultado = cadena1.upper()
#convierte a minusculas
resultado = cadena1.lower()
#convierte la primera letra a mayuscula
resultado = cadena1.capitalize()
#convierte la cadena a una sin espacios
resultado = cadena1.strip()

#Metodos que Buscan valores
#busca una cadena en otra cadena si no hay coincidencia devuelve -1
busqueda = cadena1.find('a')
#buscamos una cadena en otra cadena si no hay coincidencia lanza una exepcion
busqueda_index = cadena1.index('a')

#si es un valor deuvleve un booleano
#si es numerico devuelve true si no un false
numerico = cadena2.isnumeric()
#si es alfanumerico devuelve true si no un false(a-z)no spacios
alfa = cadena2.isalpha()

#encontramos una coincidencia de una cadena en otra cadena, devuelve las veces que coincida
contar = cadena1.count('a')
#encontramos cuantos caracteres tiene una cadena
contamos = len(cadena1)

#verificamos si una cadena empieza con una cadena dada si es asi devuelve true
empieza_con = cadena1.startswith('Ho')
#verificamos si una cadena termina con una cadena dada si es asi devuelve true
termina_con = cadena1.endswith('el')

#si se encuentra un valor que coincida se remplaza la cena original por el valor dado
cadena_nueva = cadena1.replace('Hola','Holiwis')
 
#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(' ')

print(cadena_separada)