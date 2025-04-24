class Persona:
    def __init__(self, rut, nombres, apellidos, correo, telefono):        
        self.__rut = rut
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__correo = correo
        self.__telefono = telefono
        
    @property
    def rut(self): return self.__rut
    @property
    def nombres(self): return self.__nombres
    @property
    def apellidos(self): return self.__apellidos
    @property
    def correo(self): return self.__correo
    @property
    def telefono(self): return self.__telefono
    
    def validar_rut(rut):
        return True