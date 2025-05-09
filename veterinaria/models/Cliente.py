from models.Persona import Persona

class Cliente(Persona):
    def __init__(self, rut='', nombres='', apellidos='', correo='', telefono=0, bloqueado=False):
        super().__init__(rut, nombres, apellidos, correo, telefono)
        self.__bloqueado = bloqueado
    
    @property
    def bloqueado(self): return self.__bloqueado
    @bloqueado.setter
    def bloqueado(self, bloqueado): self.__bloqueado = bloqueado
    
    def __str__(self):
        return f'Cliente: {self.rut} - {self.nombres} {self.apellidos} - {self.correo} - {self.telefono} - Bloqueado: {self.bloqueado}'
    