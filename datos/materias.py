
from modelos.materias import Materia
from datos.carreras import carreras

def generar_materias():
    materias = {}
    codigo = 100


    materias_por_carrera = {
        1: ["Introducción a la Programación", "Base de Datos I", "Matemática Discreta"],
        2: ["Anatomía I", "Práctica Deportiva"],
        3: ["Fisiología", "Enfermería General"],
        4: ["Derecho Penal", "Derecho Constitucional"],
        5: ["Diseño de Videojuegos", "Programación Gráfica"]
    }

    for cod_carrera, lista_nombres in materias_por_carrera.items():
        for nombre in lista_nombres:
            materias[codigo] = Materia(codigo, nombre, carreras[cod_carrera])
            codigo += 1

    return materias

materias = generar_materias()
def __str__(self):
        return self.nombre
