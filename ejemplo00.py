class Rectangulo: # Nombre de la clase
    # Atributos
    def __init__(self, alto, largo):
        self.__alto = alto # Atributos privados
        self.__largo = largo
    
    def calcular_area(self):
        return self.__alto * self.__largo
 
    def calcular_perimetro(self):
        return (self.__alto + self.__largo) * 2
    
    # Accediendo a alto por metodo
    def obtener_alto(self):
        return self.__alto
    # Modidificando alto por metodo    
    def establecer_alto(self, nuevo_alto):
        self.__alto = nuevo_alto
        
    # Accediendo a largo por propiedad
    @property
    def largo(self):
        return self.__largo
    # Modificar por propiedad
    @largo.setter
    def largo(self, nuevo_largo):
        self.__largo = nuevo_largo
        
r = Rectangulo(5, 3)

print(f'El area del rectangulo es: {r.calcular_area()}')
print(f'El perimetro del rectangulo es: {r.calcular_perimetro()}')
print(f'EL alto del rectangulo es: {r.obtener_alto()}') # obtener por metodo
print(f'EL largo del rectangulo es: {r.largo}') # obtener por propiedad
r.largo = 15 # Modificar por propiedad
r.establecer_alto(10) # modifcar por metodo
print(f'EL alto del rectangulo es: {r.obtener_alto()}') # obtener por metodo
print(f'EL largo del rectangulo es: {r.largo}') # obtener por propiedad