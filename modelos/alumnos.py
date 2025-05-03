class Alumno:

    def __init__(self, legajo, nombre, apellido,dni, carrera):
        self.legajo=legajo
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.carrera= carrera

    def __str__(self):
        return f"{self.nombre} {self.apellido} | DNI: {self.dni} | Legajo: {self.legajo} | Carrera: {self.carrera}"