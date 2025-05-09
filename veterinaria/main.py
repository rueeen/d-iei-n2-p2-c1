#Importar
from dao.VeterinarioDAO import VeterinarioDAO
from dao.ClienteDAO import ClienteDAO
from models.Veterinario import Veterinario
import os

# Inicio sesion
def menu_login():
    while True:
        os.system('cls')
        print('==== Menu Login ====')
        print('1. Iniciar sesion')
        print('2. Crear cuenta')
        print('0. Salir')
        
        opcion = input('Ingrese su opcion:\n')
        os.system('cls')
        
        if opcion == '1':
            print('==== Iniciar sesion ====')
            usuario = input('Ingrese usuario:\n')
            password = input('Ingrese password:\n')
            vetDao = VeterinarioDAO()
            vet = vetDao.login(usuario, password)
            if vet:
                menu_main(vet)
            else:
                print('Usuario y/o password no valido')
            
        elif opcion == '2':
            print('==== Crear cuenta ====')
            rut = input('Ingrese rut veterinario:\n')
            nombres = input('Ingrese nombres veterinario:\n')
            apellidos = input('Ingrese apellidos veterinario:\n')
            correo = input('Ingrese correo veterinario:\n')
            telefono = input('Ingrese telefono veterinario:\n')
            especialidad = input('Ingrese especialidad veterinario:\n')
            usuario = input('Ingrese usuario veterinario:\n')
            password = input('Ingrese password veterinario:\n')
            
            vetDao = VeterinarioDAO()
            vetDao.insertar_veterinario(rut, nombres, apellidos, correo, telefono, especialidad, usuario, password)
            
        elif opcion == '0':
            print('Adios...')
            break

        input('Presione enter para continuar...')

# Menu main
def menu_main(veterinario):
    while True:
        if isinstance(veterinario, Veterinario):
            os.system('cls')
            print(f'Bienvenido: {veterinario.nombres} {veterinario.apellidos}')
            print('==== Menu Principal ====')
            print('1. Crear cita medica')
            print('2. Ver citas medicas')
            print('0. Volver')
            
            opcion = input('Ingrese su opcion: ')
            os.system('cls')
            
            if opcion == '1':
                print('==== Crear Citas Medicas ====')
                rut_cliente = input('Ingrese rut cliente:\n')
                clienteDAO = ClienteDAO()
                cliente = clienteDAO.buscar_cliente(rut_cliente)
                
                if cliente:
                    print(f'Cliente encontrado: {cliente.nombres} {cliente.apellidos}')
                    
                    veterinarioDAO = VeterinarioDAO()
                    
                    veterinarioDAO.listar_veterinarios()
                    
                    rut_veterinario = input('Ingrese rut veterinario:\n')
                    fecha = input('Ingrese fecha de la cita:\n')
                    
                else:
                    print('Cliente no encontrado')
                    
                    respuesta = input('Desea crear un nuevo cliente? (s/n): ')
                    if respuesta.lower() == 's':
                        rut = input('Ingrese rut cliente:\n')
                        nombres = input('Ingrese nombres cliente:\n')
                        apellidos = input('Ingrese apellidos cliente:\n')
                        correo = input('Ingrese correo cliente:\n')
                        telefono = input('Ingrese telefono cliente:\n')
                        
                        clienteDAO.agregar_cliente(nombres, apellidos, rut, correo, telefono)
                    else:
                        print('No se ha creado el cliente')
            
            elif opcion == '2':
                print('==== Ver Citas Medicas ====')
                
            input('Presione enter para continuar...')
        
        else:
            print('Error: No se ha iniciado sesion correctamente')
            break

menu_login()