class Carrera:

    def __init__(self,codigo, nombre,materias):
        self.codigo=codigo
        self.nombre=nombre
        self.materias=materias

    def __str__(self):
        return f"{self.nombre}|Materias:{self.materias}| Codigo: {self.codigo}"