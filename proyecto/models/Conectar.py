import mysql.connector # Importando mysql.connector

class Conectar:
    # Constructor
    def __init__(self):
        # Manejo de errores sera para mas adelante
        # Metodo connect de mysql.connector
        self.__conn = mysql.connector.connect(
            host = 'localhost',
            username = 'root',
            password = '',
            database = 'tienda'
        )
        self.__cursor = self.__conn.cursor() # Crea el cursor de la bd
        
    def probando_conexion(self):
        self.__cursor.execute("SHOW TABLES") # Encargado de ejecutar sentencias SQL
        for x in self.__cursor:
            print(x)

    def ejecutar_sql(self, sql, valores): # INSERT, UPDATE, DELETE
        self.__cursor.execute(sql, valores)
        self.__conn.commit() # CONFIRMA CAMBIOS EN BASE DE DATOS
        if self.__cursor.rowcount > 0:
            return True
        return False