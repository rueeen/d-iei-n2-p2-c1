from models.Conectar import Conectar
from models.Cita import Cita

class CitaDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def agregarCita(self, idMascota, idCita, idBloque, idBox, rutVeterinario, fechaCita, confirmada, motivo):
        try:
            cita = Cita(idCita, idMascota, idBloque, idBox, rutVeterinario, fechaCita, confirmada, motivo)
            sql = "INSERT INTO Cita (idCita, idMascota, idBloque, idBox, rutVeterinario, fechaCita, confirmada, motivo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (cita.idCita, cita.idMascota, cita.idBloque, cita.idBox, cita.rutVeterinario, cita.fechaCita, cita.confirmada, cita.motivo)
            response = self.__conn.ejecutar_sql(sql, values)
            if response:
                print("Cita agregada correctamente")
            else:
                print("Error al agregar cita")
        except Exception as e:
            print(f"Error al agregar cita: {e}")
            return False
        