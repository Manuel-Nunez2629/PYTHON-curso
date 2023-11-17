#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
      print(f'Impresionante, cometiste el siguiente error: {err}')
#lanzando mi propia excepcion
'''raise ZeroDivisionError('Que baboso, dividiste por cero')'''
 
#manejandola
try:
  raise MiExcepcion("jajajaj, persona poco culta")
except:
   print('Como vas a cometer ese error?')