#Importar
from dao.VeterinarioDAO import VeterinarioDAO
from models.Veterinario import Veterinario

# Inicio sesion
def menu_login():
    print('==== Menu Login ====')
    print('1. Iniciar sesion')
    print('2. Crear cuenta')
    print('0. Salir')
    
    opcion = input('Ingrese su opcion:\n')
    
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

# Menu main
def menu_main(veterinario):
    if isinstance(veterinario, Veterinario):
        print(f'Bienvenido: {veterinario.nombres} {veterinario.apellidos}')

while True:
    menu_login()