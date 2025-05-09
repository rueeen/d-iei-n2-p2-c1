from models.Persona import Persona

class Veterinario(Persona):
    def __init__(self, rut='', nombres='', apellidos='', correo='', telefono=0, usuario='', password='', especialidad=''):
        super().__init__(rut, nombres, apellidos, correo, telefono)
        self.__usuario = usuario
        self.__password = password
        self.__especialidad = especialidad
        
    @property
    def usuario(self): return self.__usuario
    @property
    def password(self): return self.__password
    @property
    def especialidad(self): return self.__especialidad
    
    def __str__(self):
        return super().__str__() + f' - {self.especialidad}'