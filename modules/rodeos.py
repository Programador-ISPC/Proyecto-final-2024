import os
class Rodeo():
    def __init__(self):
        self.nombre = ''
        self.peso_min = ''
        self.peso_max = ''
    
    def crear_rodeo(self):
        '''
        Este método crea un nuevo rodeo.
        El usuario debe ingresar el nombre del rodeo, el peso mínimo y el peso máximo.

        TODO:
        Cuando se crea un rodeo se debe crear un rodeo por defecto llamado rechazo, cuyo valor de 
        peso minimo es 0 el el peso máximo es menor al rango del rodeo de menor peso creado por el usuario  
        '''
        print("CREAR RODEO")
        os.system("clear")
        print("Este método crea un nuevo rodeo")
        self.nombre = input("Nombre del Rodeo: ")
        self.peso_min = float(input("Ingrese peso mínimo: "))
        self.peso_max = float(input("Ingrese peso maximo: "))
        print("Rodeo creado")
    
    def modificar_rodeo(self):
        '''
        Este método modifica un rodeo.
        El usuario debe ingresar el nombre del rodeo, el peso mínimo y el peso máximo.

        TODO:
        Obtener el listado de rodeos desde la base de datos
        Evitar el solapamineto de los pasos minimos y máximos respecto a los otros rodeos.
        Mostrar la lista de rodeso con sus datos actualizados
        '''
        print("MODIFICAR RODEO")
        os.system("clear")
        print("Este método modifica un rodeo")
        self.nombre = input("Nombre del Rodeo: ")
        self.peso_min = float(input("Ingrese peso mínimo: "))
        self.peso_max = float(input("Ingrese peso maximo: "))
        print("Rodeo modificado")

    def eliminar_rodeo(self):
        '''
        Este método elimina un rodeo.
        '''
        print("Este método elimina un rodeo")
        print("Rodeo eliminado")

