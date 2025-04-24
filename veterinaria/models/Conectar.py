import mysql.connector # Importando mysql.connector

# Investigar try except con mysql.connector.error
# Aplicar try - except a clase conectar
# Apicar cerrar conexion a proyecto. self.__conn.close()
class Conectar:
    # Constructor
    def __init__(self):
        try:
            self.__conn = mysql.connector.connect(
                host = 'localhost',
                username = 'root',
                password = '',
                database = 'veterinary'
            )
            self.__cursor = self.__conn.cursor() # Crea el cursor de la bd
        except mysql.connector.Error as err:
            print(f'Se ha producido un error de base de datos: {err}')
            self.__cursor = None
        except Exception as err:
            print('Se ha producido un error inesperado.')
            self.__cursor = None
            print(f'{err}')

    def ejecutar_sql(self, sql, valores): # INSERT, UPDATE, DELETE
        try:
            if self.__cursor is None:
                print('Se ha producido un error')
                return False
            self.__cursor.execute(sql, valores) # Se encarga de ejecutars sql
            self.__conn.commit() # CONFIRMA CAMBIOS EN BASE DE DATOS
            if self.__cursor.rowcount > 0:
                return True
            return False
        except mysql.connector.Error as err:
            print(f'Se ha producido un error de base de datos: {err}')
        
    def listar(self, sql): # SELECT
        try:
            if self.__cursor is None:
                print('Se ha producido un error')
                return []
            self.__cursor.execute(sql) # Se encarga de ejecutar sql
            resultado = self.__cursor.fetchall() # [ (codigo, nombre, precio, stock), (codigo, nombre, precio, stock)]
            return resultado
        except mysql.connector.Error as err:
            print(f'Se ha producido un error de base de datos: {err}')
    
    def listarUno(self, sql, value): # SELECT
        try:
            if self.__cursor is None:
                print('Se ha producido un error')
                return ()
            self.__cursor.execute(sql, value) # Se encarga de ejecutar sql
            resultado = self.__cursor.fetchone() # (, )
            return resultado
        except mysql.connector.Error as err:
            print(f'Se ha producido un error de base de datos: {err}')