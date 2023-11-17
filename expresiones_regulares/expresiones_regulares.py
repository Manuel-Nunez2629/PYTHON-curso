#importando la calse default para pyhton manejar expresiones regulares
import re

texto = '''Hola maestro., esta es la cadena 1. , como estas mi capitan
Esta es la 23445485 linea de texto.
Y esta es la final definitiva (3.) mi capitan'''

# haciendo una busqueda simple
#resultado = re.search('Hola',texto)

#\d busca digitos numericos del 0-9
#resultado= re.findall(r'\d',texto)

#\D busca TODO MENOS digitos numericos del 0-9
#resultado= re.findall(r'\D',texto)

#\w busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado= re.findall(r'\w',texto)

#\w busca TODO menos los caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado= re.findall(r'\W',texto)


#\s busca espacios en blanco espacios, tabs, salto de linea
#resultado= re.findall(r'\s',texto)

#\S busca TODO MENOS espacios en blanco  espacios, tabs, salto de linea
#resultado= re.findall(r'\S',texto)

#. busca TODO MENOS saltos de linea
#resultado= re.findall(r'.',texto)

#\n busca saltos de linea
#resultado= re.findall(r'\n',texto)

#\ si ponemos la barra cancela todos los caracteteres especiales canceladnpo la funcion del punto y buscando puntos
#resultado = re.findall(r'\.',texto)

#armando una cadena que busque un numero,seguido de un punto y un espacio
#resultado= re.findall(f'\d\.\s',texto)

#^ busca el cominezo de la linea  buscando hola en el principio de la linea
#flags=re.M activa el multilinea y lee el inicio de nuna l;ine como es un inicio de otra linea
#resultado= re.findall(f'^Esta',texto,flags=re.M)

#$ busca el final de una linea  final
#resultado= re.findall(f'capitan$',texto,flags=re.M)

#{n} busca n cantidad de veces el valor de la izquierda
#resultado= re.findall(f'\d{3}\s',texto)

#{n,m} como n, como maximo m
#resultado= re.findall(r'\d{2,4}',texto)

#| busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)


print(resultado)