from models.Conectar import Conectar

class MascotaDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def agregarMascota(self, idMascota, rut, tipo, fechaNacimiento, estado, nombre):
        try:
            sql = "INSERT INTO Mascota (idMascota, rut, tipo, fechaNacimiento, estado, nombre) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (idMascota, rut, tipo, fechaNacimiento, estado, nombre)
            response = self.__conn.ejecutar_sql(sql, values)
            if response:
                print("Mascota agregada correctamente")
            else:
                print("Error al agregar mascota")
        except Exception as e:
            print(f"Error al agregar mascota: {e}")
            return False
        
    def listarMascotas(self):
        try:
            sql = "SELECT * FROM Mascota"
            response = self.__conn.listar(sql)
            if response:
                return response
            else:
                print("No se encontraron mascotas")
                return None
        except Exception as e:
            print(f"Error al listar mascotas: {e}")
            return None
        
    def buscarMascota(self, idMascota):
        try:
            sql = "SELECT * FROM Mascota WHERE idMascota = %s"
            response = self.__conn.listarUno(sql, (idMascota,))
            if response:
                return response
            else:
                print("Mascota no encontrada")
                return None
        except Exception as e:
            print(f"Error al buscar mascota: {e}")
            return None
        
    def buscarMascotaPorRut(self, rut):
        try:
            sql = "SELECT * FROM Mascota WHERE rut = %s"
            response = self.__conn.listarUno(sql, (rut,))
            if response:
                return response
            else:
                print("Mascota no encontrada con el rut proporcionado")
                return None
        except Exception as e:
            print(f"Error al buscar mascota por rut: {e}")
            return None