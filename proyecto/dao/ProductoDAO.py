from models.Conectar import Conectar # Importa clase Conectar dentro de ProductoDAO

class ProductoDAO:
    def __init__(self):
        self.__conectar = Conectar() # Instancia objeto Conectar para ejecutar conexion a base de datos
        
    def insertar_producto(self, producto): 
        # Utilizando SQL
        sql = """
            INSERT INTO producto (codigo, nombre, precio, stock) 
            VALUES (%s, %s, %s, %s)
            """
        # Crear tupla de datos con objeto producto
        valores = (
            producto.codigo,
            producto.nombre,
            producto.precio,
            producto.stock
        )
        
        # Ejecutando sentencia sql DEVUELVE TRUE o FALSE
        respuesta = self.__conectar.ejecutar_sql(sql, valores)
        if respuesta:
            print('Se ha registrado el producto en la base de datos')
        else:
            print('No se logro registrar el producto')