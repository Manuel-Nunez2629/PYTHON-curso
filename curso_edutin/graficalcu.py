#biblioteca tkinter e importamos todo de la biblioteca
from tkinter import *


#instancia raiz de la aplicacion
root = Tk()

#Titulo de la aplicacion
root.title("Calculadora")

#bandeja de entrada de datos guardada en variable display
display= Entry(root)
#ubicacion del display columspan es abarcar, sitcky el ancho de todo el ancho posible de la columna
display.grid(row=1,columnspan=6, sticky=W+E)
#iniciamos el indice
i=0
#funcion para obtener los numeros o ingresar indice aumenta cada que ingresamos un valor i=i+1
def obtenernumeros(n):
    global i
    display.insert(i,n)
    i+=1

def operaciones(operador):
    global i
    operador_len=len(operador)
    display.insert(i,operador)
    i+=operador_len

def limpiar():
    display.delete(0,END)

def eliminar():
    estado=display.get() 
    if len(estado):
        estado_nuevo=estado[:-1]
        limpiar()
        display.insert(0,estado_nuevo)
    else:
        limpiar()
        display.insert(0,'Error')

def calculo():
    estado = display.get()
    try:
        expresionmate = compile(estado, 'app.py', 'eval')
        result = eval(expresionmate)
        limpiar()
        display.insert(0,result)

    except:
        limpiar()
        display.insert(0,"error")


#botones
#donde esta montado es root y el texto es numero y el grid es para saber que poscicion estara en la ventana
#"command=" es un parámetro que se utiliza para asignar una función que se ejecutará cuando un elemento interactivo, como un botón, sea presionado o activado
#lambda se utilizan cuando necesitas una función temporal o pequeña que no requiere un nombre definido
Button(root, text= "1",command=lambda:obtenernumeros(1)).grid(row=6,column=0, sticky=W+E)
Button(root, text= "2",command=lambda:obtenernumeros(2)).grid(row=6,column=1, sticky=W+E)
Button(root, text= "3",command=lambda:obtenernumeros(3)).grid(row=6,column=2, sticky=W+E)
Button(root, text= "4",command=lambda:obtenernumeros(4)).grid(row=5,column=0, sticky=W+E)
Button(root, text= "5",command=lambda:obtenernumeros(5)).grid(row=5,column=1, sticky=W+E)
Button(root, text= "6",command=lambda:obtenernumeros(6)).grid(row=5,column=2, sticky=W+E)
Button(root, text= "7",command=lambda:obtenernumeros(7)).grid(row=4,column=0, sticky=W+E)
Button(root, text= "8",command=lambda:obtenernumeros(8)).grid(row=4,column=1, sticky=W+E)
Button(root, text= "9",command=lambda:obtenernumeros(9)).grid(row=4,column=2, sticky=W+E)
Button(root, text= "0",command=lambda:obtenernumeros(0)).grid(row=7,column=1, sticky=W+E)


#botones de operaciones
Button(root, text= "AC",command=lambda:limpiar()).grid(row=7,column=0, sticky=W+E)
Button(root, text= ".",command=lambda:operaciones(".")).grid(row=7,column=2, sticky=W+E)
Button(root, text= "+",command=lambda:operaciones("+")).grid(row=6,column=3, sticky=W+E)
Button(root, text= "-",command=lambda:operaciones("-")).grid(row=5,column=3, sticky=W+E)
Button(root, text= "=",command=lambda:calculo()).grid(row=7,column=3, sticky=W+E)
Button(root, text= "✶",command=lambda:operaciones("*")).grid(row=4,column=3, sticky=W+E)

Button(root, text= "%",command=lambda:operaciones("%")).grid(row=2,column=0, sticky=W+E)
Button(root, text= "x²",command=lambda:operaciones("**2")).grid(row=2,column=1, sticky=W+E)
Button(root, text= "√x",command=lambda:operaciones("nose")).grid(row=2,column=2, sticky=W+E)
Button(root, text= "⮘",command=lambda:eliminar()).grid(row=2,column=3, sticky=W+E)

Button(root, text= "(",command=lambda:operaciones("(")).grid(row=3,column=0, sticky=W+E)
Button(root, text= ")",command=lambda:operaciones(")")).grid(row=3,column=1, sticky=W+E)
Button(root, text= ",",command=lambda:operaciones(",")).grid(row=3,column=2, sticky=W+E)
#Button(root, text= "C").grid(row=2,column=3, sticky=W+E)
Button(root, text= "÷",command=lambda:operaciones("/")).grid(row=3,column=3, sticky=W+E)

root.mainloop()

