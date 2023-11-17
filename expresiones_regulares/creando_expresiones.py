import re
#detectando un numero CABA y ocultandolo
texto = "Hola Pedro, mi numero es: +507 6609-5551"

pattern = r'\+\d{1,3}\s\d{4}-\d{4}'

reemplazo = re.sub(pattern,'(Numero oculto)',texto)

print (reemplazo)