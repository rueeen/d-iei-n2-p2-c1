from models.Producto import Producto
from dao.ProductoDAO import ProductoDAO

while True:
    print('==== Menu de acciones ====')
    print('1. Agregar producto')
    
    opcion = input('Ingrese su opcion:\n')
    
    if opcion == '1':
        print('==== Ingresando producto ====')
        codigo = input('Ingrese codigo producto:\n')
        nombre = input('Ingrese nombre de producto:\n')
        precio = float(input('Ingrese precio de producto:\n'))
        stock = int(input('Ingrese stock de producto:\n'))
        
        producto = Producto(codigo, nombre, precio, stock)
        
        dao = ProductoDAO()
        dao.insertar_producto(producto)