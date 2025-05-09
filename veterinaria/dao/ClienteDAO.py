from models.Conectar import Conectar
from models.Cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.__conn = Conectar()
        
    def agregar_cliente(self, nombres, apellidos, rut, correo, telefono, bloqueado=False):
            # Antes de crear Cliente por herencia se crea primero Persona
            cliente = Cliente(rut, nombres, apellidos, correo, telefono, bloqueado)
            # Validar datos de persona
            sql = '''
                INSERT INTO persona(rut, nombres, apellidos, correo, telefono)
                VALUES (%s, %s, %s, %s, %s)
            '''
            
            respuesta = self.__conn.ejecutar_sql(sql, (cliente.rut, cliente.nombres, cliente.apellidos, cliente.correo, cliente.telefono))
        
            if respuesta:
                sql = '''
                    INSERT INTO cliente(rut, bloqueado)
                    VALUES (%s, %s)'''
                respuesta = self.__conn.ejecutar_sql(sql, (cliente.rut, cliente.bloqueado))
                if respuesta:
                    print('Se ha registrado a cliente exitosamente')
            else:
                print('No se pudo crear al cliente')
                
    def listar_clientes(self):
        sql = '''
            SELECT persona.rut, persona.nombres, persona.apellidos, persona.correo, persona.telefono, cliente.bloqueado
            FROM cliente
            INNER JOIN persona ON cliente.rut = persona.rut
        '''
        resultado = self.__conn.listar(sql)
        lista_clientes = []
        for fila in resultado:
            cliente = Cliente(rut=fila[0], nombres=fila[1], apellidos=fila[2], correo=fila[3], telefono=fila[4], bloqueado=fila[5])
            lista_clientes.append(cliente)
        return lista_clientes
        
    def buscar_cliente(self, rut):
        sql = '''
            SELECT persona.rut, persona.nombres, persona.apellidos, persona.correo, persona.telefono, cliente.bloqueado
            FROM cliente
            INNER JOIN persona ON cliente.rut = persona.rut
            WHERE cliente.rut = %s
        '''
        resultado = self.__conn.listarUno(sql, (rut,))
        if resultado:
            cliente = Cliente(rut=resultado[0], nombres=resultado[1], apellidos=resultado[2], correo=resultado[3], telefono=resultado[4], bloqueado=resultado[5])
            return cliente
        return None