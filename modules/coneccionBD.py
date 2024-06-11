import mysql.connector
from mysql.connector import Error
from dbsetup_script import dbsetup_script

class GestionBD:
    def __init__(self):
        self.connection = None
        self.setup_script = dbsetup_script

    def connect(self):
        """Establece la conexión a la base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',  
                database='nombre_base_datos',  
                user='tu_usuario',  
                password='tu_contraseña'  
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        """Cierra la conexión a la base de datos"""
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión a la base de datos cerrada")

    def execute_query(self, query):
        """Ejecuta una consulta y retorna los resultados"""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            # Si es una consulta de selección, retornar los resultados
            if query.strip().lower().startswith("select"):
                results = cursor.fetchall()
                return results
            # Si es una consulta de modificación, confirmar los cambios
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        finally:
            cursor.close()

    def setup_database(self):
        """
    Ejecuta el script SQL proporcionado para crear el esquema de la base de datos si aún no existe.
        """
        self.connect()
        cursor = self.connection.cursor()
        try:
            for statement in self.setup_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)
            self.connection.commit()
            print("Base de datos creada.")
        except mysql.connector.Error as err:
            print(f"Error al crear la base de datos: {err}")
        finally:
            cursor.close()
