from modelos.alumnos import Alumno
from datos.carreras import carreras

alumnos = {
    12345678: Alumno(1, "Juan", "Pérez", 12345678, carreras[1]),
    23456789: Alumno(2, "Ana", "Gómez", 23456789, carreras[2]),
    34567890: Alumno(3, "Luis", "Martínez",34567890,  carreras[1]),
}