import os

class Animales():
    def __init__(self):
        self.caravana = ''
        self.peso = ''
        self.fecha = ''
    
    def alta_caravana(self):
        '''
        Este método da de alta la caravana asociada a un animal. 
        El usuario debe ingresar el número de caravana, peso, fecha del alta.

        TODO:
        No puede registrarse caravanas si no ha rodeos creados
        Agregar lógica para asignar el animal a un rodeo de acuerdo a su peso
        El estado de la caravana al registrarse es activa
        Si el animal no alcanza el peso mínimo de ninguna categoria de rodeo se rechaza
        '''
        print("ALTA DE CARAVANA")
        os.system("clear")
        print("Este método crea una nueva caravana")
        self.caravana = input("Ingrese caravana: ")
        self.peso = float(input("Ingrese el peso: "))
        self.fecha = input("Ingrese la fecha de la caravana: ")
        print("Caravana creada")

    def registro_peso(self):
        '''
        Este método registra el peso de un animal en una fecha

        TODO:
        Verificar que caravana existe
        Verificar que la caravana no ha sido dada de baja
        Guardar el nuevo registro en la tabla correspondiente
        Actualizar el peso relacionado a la caravana de la caravana
        '''
        print("REGISTRO DE PESO")
        os.system("clear")
        print("Este método registra el peso de la caravana")
        self.caravana = input("Ingrese la caravana: ")
        self.peso = float(input("Ingrese el peso del animal: "))
        self.fecha = input("Ingrese la fecha del pesaje: ")
        print("Peso registrado")

    def baja_caravana(self):
        '''
        Este método da de baja la caravana asociada a un animal.
        El usuario debe ingresar el número de caravana, la razón y la fecha de baja.
        '''
        print("BAJA DE CARAVANA")
        os.system("clear")
        print("Este método elimina una caravana")
        self.caravana = input("Ingrese el nombre de la caravana: ")
        self.fecha = input("Ingrese fecha de la baja: ")
        razon = input("Razón de la baja: ")
        print("Caravana dada de baja")