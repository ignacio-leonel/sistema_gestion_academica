from modelos.alumnos import Alumno 
from datos.alumnos import alumnos

def crear_alumno():
    legajo= input("ingrese el legajo: ")
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    dni = input("ingrese el dni: ")
    carrera = input("ingrese la carrera: ")
    
    nuevo_alumno = Alumno(legajo, nombre,apellido,dni, carrera)
    

    return nuevo_alumno



def mostrar_alumnos():

    for alumno in alumnos.values():
        print(f"Legajo: {alumno.legajo}, Nombre: {alumno.nombre}, Apellido: {alumno.apellido}, Carrera: {alumno.carrera.nombre}")


def buscar_alumno_dni():
    encontrado=False
    dni=int(input("ingrese el dni"))
    for alumno in alumnos.values(): 
        if alumno.dni == dni:
            print(f"El alumno con DNI {dni} es {alumno.nombre} {alumno.apellido}")
            encontrado = True
            break

    if not encontrado:
        print("DNI no encontrado.")

    return alumno()

def buscar_alumno_carrera():

    encontrado=False
    carr=input("ingrese la carrera: ")
    print(f"Los alumnos de la carrera {carr} son:\n")
    
    
    for alumno in alumnos.values(): 
        if alumno.carrera.nombre.lower() == carr.lower():
            print(f"\n {alumno.nombre} {alumno.apellido} {alumno.dni}")
            encontrado = True
            

    if not encontrado:
        print("carrera no encontrada o sin alumnos.")

