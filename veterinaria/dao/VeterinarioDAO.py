from models.Persona import Persona
from models.Veterinario import Veterinario
from models.Conectar import Conectar

class VeterinarioDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def insertar_veterinario(self, rut, nombres, apellidos, correo, telefono, especialidad, usuario, password):
        # Antes de crer veterinario por herencia se crea primero persona
        persona = Persona(rut, nombres, apellidos, correo, telefono)
        # Validar datos de persona
        sql = '''
            INSERT INTO persona(rut, nombres, apellidos, correo, telefono)
            VALUES (%s, %s, %s, %s, %s)
        '''
        respuesta = self.__conn.ejecutar_sql(sql, (persona.rut, persona.nombres, persona.apellidos, persona.correo, persona.telefono))
        
        if respuesta:
            sql = '''
                INSERT INTO veterinario(rutVeterinario, usuario, password, especialidad)
                VALUES (%s, %s, %s, %s)'''
            respuesta = self.__conn.ejecutar_sql(sql, (persona.rut, usuario, password, especialidad))
            if respuesta:
                print('Se ha registrado al veterinario exitosamente')
        else:
            print('No se pudo crear al veterinario')
            
    def login(self, usuario, password):
        # validar datos
        sql = '''
            SELECT persona.nombres, persona.apellidos
            FROM veterinario
            INNER JOIN persona ON veterinario.rutVeterinario = persona.rut
            WHERE veterinario.usuario = %s 
            AND veterinario.password = %s
            '''
        resultado = self.__conn.listarUno(sql, (usuario, password))
        if resultado: # (nombre, apellido)
            return Veterinario(nombres=resultado[0], apellidos=resultado[1])