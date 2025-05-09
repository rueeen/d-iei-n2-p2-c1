class Mascota:
    def __init__(self, idMascota, rut , tipo, fechaNacimiento, estado, nombre):
        self.__idMascota = idMascota
        self.__rut = rut
        self.__tipo = tipo
        self.__fechaNacimiento = fechaNacimiento
        self.__estado = estado
        self.__nombre = nombre
        
    @property
    def idMascota(self): return self.__idMascota
    
    @property
    def rut(self): return self.__rut
    
    @property
    def tipo(self): return self.__tipo
    
    @property
    def fechaNacimiento(self): return self.__fechaNacimiento
    
    @property
    def estado(self): return self.__estado
    
    @property
    def nombre(self): return self.__nombre
    
    @idMascota.setter
    def idMascota(self, idMascota): self.__idMascota = idMascota
    
    @rut.setter
    def rut(self, rut): self.__rut = rut    
    
    @tipo.setter
    def tipo(self, tipo): self.__tipo = tipo
    
    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento): self.__fechaNacimiento = fechaNacimiento
    
    @estado.setter
    def estado(self, estado): self.__estado = estado
    
    @nombre.setter
    def nombre(self, nombre): self.__nombre = nombre
    
    def __str__(self):
        return f'Mascota: {self.idMascota} - {self.rut} - {self.tipo} - {self.fechaNacimiento} - {self.estado} - {self.nombre}'