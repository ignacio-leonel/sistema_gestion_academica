from modelos.alumnos import Alumno 
from datos.alumnos import alumnos
import servicios.metodos_alumnos as ma

def menu_admin():
    print("hola admin")


print("1 - Ingresar Alumno")
print("2 - Modificar Datos de Alumno")
print("3 - Crear Carrera")
print("4 - Añadir materias a Carrera")
print("5 - Modificar Notas")
print("6 - Buscar Alumno DNI")



opcion=int(input("seleccione la opcion deseada: "))

if(opcion==6):
    ma.buscar_alumno_dni()



