from models.Conectar import Conectar
from models.Box import Box

class BoxDAO:
    def __init__(self):
        self.__conn = Conectar()

    def listar_boxes(self):
        sql = "SELECT idBox FROM box"
        resultado = self.__conn.listar(sql)
        lista_boxes = []
        for fila in resultado:
            box = Box(idBox=fila[0])
            lista_boxes.append(box)
        return lista_boxes

    def buscar_box(self, id_box):
        sql = "SELECT idBox FROM box WHERE idBox = %s"
        resultado = self.__conn.listarUno(sql, (id_box,))
        if resultado:
            return Box(idBox=resultado[0])
        return None
