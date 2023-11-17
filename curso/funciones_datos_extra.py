#creando una funcion que dice una frase
#creadno la misma funcion conun parametro opcional y un valor por defecvto
def frase(nombre,apellido,adjetivo='Tonto'):
    return f'Hola {nombre} {apellido}, como estas {adjetivo}'
#se puede no pasar parametro para adjetvio porque ya esta definido por defecto en la funcion
frase_resultante = frase('Manuel','Nunez')
print(frase_resultante)