class Producto:
    # constructor
    def __init__(self, codigo, nombre, precio, stock):
        # Atributos
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        
    # Propiedad getter
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nombre(self):
        return self.__nombre  
    @property
    def precio(self):
        return self.__precio  
    @property
    def stock(self):
        return self.__stock  
        
    # Metodos
    def crear_producto(self):
        pass
    
    def ver_producto(self):
        pass
    
    def listar_productos(self):
        pass