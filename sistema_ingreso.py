
print('Bienvenido al sistema de matricula')

base_datos={'Nanu2629':'hola234',
           'Sofybc':'clirbi'}

usuario,contraseña = base_datos

def inicio_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario not in base_datos:
        print(f'No se encuentra este nombre de usuario\nSi no ha creado uno registre su nombre de usuario')
        reg = int(input('¿Desea ir a registro de usuario?\n1.Si\n2.No\n'))
        if reg == 1:
            print('Redireccionando al Sistema de Registro...')
            registro()
        elif reg == 2:
            print('Ingrese nuevamente su nombre de usuario.')
            inicio_sesion()
        else:
            print('Valor invalido ingrese un valor dentro del parametro.')
    else:
        contador = 3
        while contador > 0:
            contraseña = input('Ingrese su contraseña: ')
            if contraseña != base_datos[usuario]:
                contador -=1
                print(f'Contraseña incorrecta\nTe quedan {contador} intentos.')
                
            else:
                
                print('Acesso permitido')
                print(base_datos)
                Inicio()
        if contador == 0:
            print('Intentos maximos permitidos.\nRegresando a la pantalla de inicio')
            Inicio()
            
def registro():
    print(f'Sistema de Registro\n')
    usuario = input('Ingrese un Nombre de Usuario: ')
    if usuario in base_datos:
        print('Este nombre de usuario ya ha sido registrado intente otra vez.')
        registro()
    else:
        contraseña = input('Ingrese una contraseña: ')
        base_datos[usuario] = contraseña
        print(f'Añadida correctamente\nBienvenido {usuario}')
        print(base_datos)
        inicio_sesion()
        
def Inicio():
    opcion = True      
    while opcion:    
        print('elige una opcion\n1. para inicio de sesion\n2. Para Registrar un nuevo usuario:\n')
        eleccion = ''
        while eleccion not in ("1","2"):
            eleccion = input("--> ")
            if eleccion == '1':
                opcion = False
                print('Redireccionando al inicio de sesion...')
                inicio_sesion()
            elif eleccion == '2':
                opcion = False
                print('Redireccionando al Sistema de Registro')
                registro()
            else:
                print('Elige una opcion valida.')   
            
     
        
Inicio()      
        
