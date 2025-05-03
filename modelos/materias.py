class Materia:
    def __init__(self, codigo, nombre,carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.carrera=carrera

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.carrera.nombre}"
