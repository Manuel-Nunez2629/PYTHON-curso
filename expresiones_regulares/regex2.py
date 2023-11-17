import re 

#la cadena qen la que se buscara los patrones
text = 'La fecha es 23/06/2023 y el telefono es +1-555-555-5555'

#el patron a buscar
pattern = r'\d{2}/\d{2}/\d{4}'

#el texto con el que remplazara el patron 
replacemente = 'Fecha oculta'

#Reemplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern, replacemente,text)

#imprimir el resultado
print(f'Texto modificado: {new_text}')