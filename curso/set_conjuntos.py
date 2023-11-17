#creando set o conjuntos con la funcion set
#conjunto = set({'manuel','nunez'})
#sepuede agregar tuplas al set dentro pero no diccionarios ni listas porque son mutables y los set y tuplas no
#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1','dato2'])
conjunto2 = {conjunto1,'dato3'}

#creando conjuntos con los parentesis
conjunto = {'manuel', 'nunez'}

#teoria de conjuntos
#false porque el conjunto 1 tiene mas datos que el conjunto 2
set={1,4,5,7,8,9}
set2={1,4,5}
#funcion de si es un subconjunto
resultado=set.issubset(set2)
#funcion de si es un superconjunto
resultado2=set.issuperset(set2)
#verificando si hay mas numeros en el conjunto1 que el conjunto2
resultado3=set>=set2


#verificar si hay algun numero en comun
#no tiene que tener ningun numero en comuun para que nos diga que es True
resultado4=set.isdisjoint(set2)

print(resultado4)