from modelos.carreras import Carrera
from modelos.materias import Materia
from modelos.alumnos import Alumno

import servicios.metodos_alumnos as ma



def anotar_alumno_materia():
    alumno= ma.buscar_alumno_dni()
    print(f"seleccione la materia para anotar al alumno {alumno.nombre}{alumno.apellido}{alumno.dni}")
   
    for materia in materias.length:
        print(materia.nombre)
        selector= int(input("ingrese la opcion deseada: "))
    for materia in materias.length:
        if (selector==materia.codigo ):
            carrera.materias.append(materia)


