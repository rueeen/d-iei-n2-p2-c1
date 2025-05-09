from models.Conectar import Conectar
from models.Bloque import BloqueHorario

class BloqueHorarioDAO:
    def __init__(self):
        self.__conn = Conectar()

    def obtener_bloques_disponibles(self, rut_veterinario, fecha_cita):
        sql = '''
            SELECT bh.idBloque, bh.horaInicio, bh.horaFin
            FROM bloquehorario bh
            WHERE bh.idBloque NOT IN (
                SELECT c.idBloque
                FROM cita c
                WHERE c.rutVeterinario = %s AND c.fechaCita = %s
            )
        '''
        resultados = self.__conn.listar_con_parametros(sql, (rut_veterinario, fecha_cita))
        bloques = []
        for fila in resultados:
            bloque = BloqueHorario(idBloque=fila[0], horaInicio=fila[1], horaFin=fila[2])
            bloques.append(bloque)
        return bloques

