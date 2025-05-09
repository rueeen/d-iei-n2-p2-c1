# campos bd Cita idMascota	idCita	idBloque	idBox	rutVeterinario	fechaCita	confirmada	motivo

class Cita:
    def __init__(self, idCita, idMascota, idBloque, idBox, rutVeterinario, fechaCita, confirmada, motivo):
        self.__idCita = idCita
        self.__idMascota = idMascota
        self.__idBloque = idBloque
        self.__idBox = idBox
        self.__rutVeterinario = rutVeterinario
        self.__fechaCita = fechaCita
        self.__confirmada = confirmada
        self.__motivo = motivo    
    
    @property
    def idCita(self): return self.__idCita

    @idCita.setter
    def idCita(self, idCita): self.__idCita = idCita

    @property
    def idMascota(self): return self.__idMascota

    @idMascota.setter
    def idMascota(self, idMascota): self.__idMascota = idMascota

    @property
    def idBloque(self): return self.__idBloque

    @idBloque.setter
    def idBloque(self, idBloque): self.__idBloque = idBloque

    @property
    def idBox(self): return self.__idBox

    @idBox.setter
    def idBox(self, idBox): self.__idBox = idBox

    @property
    def rutVeterinario(self): return self.__rutVeterinario

    @rutVeterinario.setter
    def rutVeterinario(self, rutVeterinario): self.__rutVeterinario = rutVeterinario

    @property
    def fechaCita(self): return self.__fechaCita

    @fechaCita.setter
    def fechaCita(self, fechaCita): self.__fechaCita = fechaCita

    @property
    def confirmada(self): return self.__confirmada

    @confirmada.setter
    def confirmada(self, confirmada): self.__confirmada = confirmada

    @property
    def motivo(self): return self.__motivo

    @motivo.setter
    def motivo(self, motivo): self.__motivo = motivo
