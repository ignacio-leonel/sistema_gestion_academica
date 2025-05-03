#importacion e modelos

from modelos.alumnos import Alumno
from modelos.usuarios import Usuario
from modelos.carreras import Carrera

#importacion de datos

from datos.materias import materias
from datos.alumnos import alumnos


#importacion de metodos
import servicios.metodos_alumnos as ma
import servicios.metodos_carreras as mc
#ma.crear_alumno()
#ma.buscar_alumno_dni()
#ma.mostrar_alumnos()
#ma.buscar_alumno_carrera()

mc.anotar_alumno_materia()