from models.Conectar import Conectar
from models.Bloque import BloqueHorario

class BloqueDAO:
    def __init__(self):
        self.__conn = Conectar()
        
        
    def listarBloques(self):
        try:
            sql = "SELECT * FROM bloquehorario"
            response = self.__conn.ejecutar_sql(sql)
            bloques = []
            for row in response:
                bloque = BloqueHorario(row[0], row[1], row[2])
                bloques.append(bloque)
            return bloques
        except Exception as e:
            print(f"Error al listar bloques: {e}")
            return None