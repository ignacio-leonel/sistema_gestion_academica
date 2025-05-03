#esto es a modo de prueba para estructurar bien cada parte del desarrollo
# la idea es de que luego, al ingresar el usuario y contraseña el sistema 
# reconozca el tipo de usuario y muestre el menu correspondiente.
from menus.menu_admin import menu_admin 
from menus.menu_docente import menu_docente 
from menus.menu_estudiante import menu_estudiante

print("Sistema de Gestión Estudiantil")

print("opcion 1: Administrador")
print("opcion 2: Docente")
print("opcion 3: Estudiante")


rol = int(input("Seleccione su tipo de Usuario (1: Administrador, 2: Docente, 3: Estudiante): "))

while rol not in [1, 2, 3]:
    print("Opción inválida. Intenta de nuevo.")
   
    rol = int(input("Seleccione su tipo de Usuario (1: Administrador, 2: Docente, 3: Estudiante): "))

if rol == 1:
        menu_admin()
elif rol == 2:
        menu_docente()
elif rol == 3:
        menu_estudiante()
