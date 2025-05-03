def listar_carreras(carreras_dict):
    if not carreras_dict:
        print("No hay carreras cargadas.")
        return

    print("\nListado de Carreras:")
    for codigo, carrera in carreras_dict.items():
        print(f"{codigo} - {carrera.nombre}")

def listar_materias(materias_dict):
    if not materias_dict:
        print("No hay materias cargadas.")
        return

    print("\nMaterias por Carrera:")
    for codigo, materias in materias_dict.items():
        print(f"\nCarrera {codigo}:")
        for materia in materias:
            print(f" - {materia}")