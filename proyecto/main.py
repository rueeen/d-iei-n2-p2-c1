from dao.ProductoDAO import ProductoDAO
import os

while True:
    os.system('cls') # Limpia consola
    print('==== Menu de acciones ====')
    print('1. ✅ Agregar producto')
    print('2. Mostrar productos')        
    print('3. Actualizar productos')
    print('4. Eliminar productos')
    print('0. Salir')
    
    opcion = input('Ingrese su opcion:\n')
    os.system('cls') # Limpia consola
    
    if opcion == '1':
        print('==== Ingresando producto ====')
        codigo = input('Ingrese codigo producto:\n').lower() # abc 
        nombre = input('Ingrese nombre de producto:\n').capitalize()
        precio = float(input('Ingrese precio de producto:\n'))
        stock = int(input('Ingrese stock de producto:\n'))
        
        dao = ProductoDAO()
        dao.insertar_producto(codigo, nombre, precio, stock)
    
    elif opcion == '2':
        print('==== Mostrar producto ====')
        dao = ProductoDAO()
        dao.listar_productos()
    
    elif opcion == '3':
        print('==== Actualizar producto ====')
        # buscar un producto
        codigo = input('Ingrese codigo a modificar:\n').lower()
        # nuevo nombre producto
        nombre = input('Ingrese nuevo nombre:\n').capitalize()
        dao = ProductoDAO()
        dao.modificar_nombre_producto(codigo, nombre)
    
    elif opcion == '4':
        print('==== Eliminar productos ====')
        codigo = input('Ingrese codigo a eliminar:\n').lower()
        dao = ProductoDAO()
        dao.eliminar_producto(codigo)
        
    elif opcion == '0':
        print('Saliendo sistema...')
        break
    
    else:
        print('Ingrese una opcion valida...')
    
    input('Presione enter para continuar...')