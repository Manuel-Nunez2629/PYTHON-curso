#creando una lista con el metodo list()
lista = list(['Manuel','Jose',26,65,58])
#devuelve la cantaidad de elementos dentro de la lista
cantidad=len(lista)
#agregar un elemento a una lista
lista.append('JAJAJA')
#agregar un elemento a la lista en un indice especifico
#Lista.inster(indice,y valoragregar)
lista.insert(2,'MAMAMA')
#agregamos varios elementos a la lista
lista.extend([45,65,'Joaquin'])
#eliminamos un elemento de la lista
#eliminar los ultimos valores agregados lista.pop(-1)para el ultimo o lista.pop(-2) para el penultimo y asi 
lista.pop(5)
#remueve un elemento de la lista por su valor en especifico si no encuentra tira una exepcion list.remove() takes exactly one argument
lista.remove("Manuel")
#remplaza el valor de la lista con uno nuevo
lista[0]='Jose'
#presentar valores especificos en una lsita
print(lista[1:3])
#se agregan varios elementos a una lista de un conjunto a una lista
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#elimina la lista o todos los elementos
#lista.clear()

lista2=[25,65,788,41,2]
#Ordena una lista de forma ascendente a descendente, no soporta cadena de texto Booleanos si
lista2.sort() #[2, 25, 41, 65, 788]
#si utilizamos el revertrue lo ordena de forma decendente a ascendente
lista2.sort(reverse=True) #[788, 65, 41, 25, 2]

#invierte los elementos de la lista
lista2.reverse() #[2, 41, 788, 65, 25]


#verificando si un elemento se encuentra en la lista si o encuentra muestra una exepcion en las tuplas solo se cuenta o se busca pero no se puede alterar
elemento_encontrado = lista.index('Jose')


print(elemento_encontrado)