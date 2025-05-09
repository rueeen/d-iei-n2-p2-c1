# campos bloquehorario idBloque horaInicio horaFin

class BloqueHorario:
    def __init__(self, idBloque, horaInicio, horaFin):
        self.__idBloque = idBloque
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin

    @property
    def idBloque(self): return self.__idBloque

    @idBloque.setter
    def idBloque(self, idBloque): self.__idBloque = idBloque

    @property
    def horaInicio(self): return self.__horaInicio

    @horaInicio.setter
    def horaInicio(self, horaInicio): self.__horaInicio = horaInicio

    @property
    def horaFin(self): return self.__horaFin

    @horaFin.setter
    def horaFin(self, horaFin): self.__horaFin = horaFin