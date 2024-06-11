import os
from coneccionBD import GestionBD

class Animales():
    def __init__(self):
        self.caravana = ''
        self.peso = ''
        self.fecha = ''
        self.razone = ''
        self.dbmanager = GestionBD() 
    
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
        self.fecha = input("Ingrese la fecha de ingreso: ")
        
        # Validar que existan rodeos creados
        self.dbmanager.connect()
        rodeos = self.dbmanager.execute_query(
            "SELECT COUNT(*) FROM Rodeos"
        )
        if rodeos[0][0] == 0:
            print("No hay rodeos creados, no se puede registrar la caravana.")
            self.dbmanager.disconnect()
            return

        # Asignar el animal a un rodeo de acuerdo a su peso
        rodeo = self.dbmanager.execute_query(
            f"SELECT id FROM Rodeos WHERE peso_minimo <= {self.peso} AND peso_maximo >= {self.peso}"
        )
        if not rodeo:
            print("El peso del animal no alcanza el mínimo requerido para ningún rodeo. Caravana rechazada.")
            self.dbmanager.disconnect()
            return

        rodeo_id = rodeo[0][0]

        # Insertar la caravana en la base de datos
        self.dbmanager.execute_query(
            f"INSERT INTO Caravanas (caravana, peso, fecha_alta, activa, rodeo_id) 
            VALUES ('{self.caravana}', {self.peso}, '{self.fecha}', true, {rodeo_id})"
        )
        self.dbmanager.disconnect()
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
        
        # Verificar que la caravana existe y está activa
        self.dbmanager.connect()
        caravana = self.dbmanager.execute_query(
            f"SELECT * FROM Caravanas WHERE caravana = '{self.caravana}' AND activa = true"
        )
        if not caravana:
            print("Caravana no existe o ha sido dada de baja.")
            self.dbmanager.disconnect()
            return

        # Insertar el nuevo registro de peso
        self.dbmanager.execute_query(
            f"INSERT INTO Pesajes (caravana, peso, fecha) 
            VALUES ('{self.caravana}', {self.peso}, '{self.fecha}')")

        self.dbmanager.disconnect()
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
        self.razon = input("Razón de la baja: ")
        
        # Verificar que la caravana existe y está activa
        self.dbmanager.connect()
        caravana = self.dbmanager.execute_query(
            f"SELECT * FROM Caravanas WHERE caravana = '{self.caravana}' AND activa = true"
        )
        if not caravana:
            print("Caravana no existe o ya ha sido dada de baja.")
            self.dbmanager.disconnect()
            return

        # Dar de baja la caravana
        self.dbmanager.execute_query(
            f"UPDATE Caravanas SET activa = false, fecha_baja = '{self.fecha}', razon_baja = '{self.razon}' WHERE caravana = '{self.caravana}'"
        )
        self.dbmanager.disconnect()
        print("Caravana dada de baja")
