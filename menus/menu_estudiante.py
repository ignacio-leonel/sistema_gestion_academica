from modelos.alumnos import Alumno 
import servicios.metodos_alumnos as mag

def menu_estudiante():
    print("hola estudiante")
    
    

    print("1 - Consultar Notas")
    print("2-  Listar materias de la carrera")
    print("3 - Porcentaje de avance en la carrera")


    opcion=int(input("seleccione la opcion deseada: "))
