from modelos.alumnos import Alumno 
from datos.conexion import conexion

def crear_alumno():
    legajo= input("ingrese el legajo: ")
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    dni = input("ingrese el dni: ")
    carrera = input("ingrese la carrera: ")
    
    nuevo_alumno = Alumno(legajo, nombre,apellido,dni, carrera)
    

    return nuevo_alumno



def mostrar_alumnos():

    conn = conexion()
    cursor = conn.cursor()
    
    # Ejecutamos la consulta para obtener todos los alumnos
    cursor.execute("SELECT * FROM alumnos")
    
    # Obtenemos todos los resultados
    resultados = cursor.fetchall()

    if resultados:  # Comprobamos si hay resultados
        print("Alumnos encontrados:")
        for alumno in resultados:
            # Imprimir cada alumno en formato legible
            print(f"Legajo: {alumno[0]}, Nombre: {alumno[1]}, Apellido: {alumno[2]}, DNI: {alumno[3]}, Carrera: {alumno[4]}")
           
    else:
        print("No se encontraron alumnos")

    return resultados  # Devolvemos la lista de alumnos

def buscar_alumno_dni():
    conn = conexion()
    cursor = conn.cursor()
    
    dni_buscado = input("Ingrese el DNI del alumno: ")
    cursor.execute("SELECT * FROM alumnos WHERE dni = ?", (dni_buscado,))
    resultado = cursor.fetchone()  # Aquí guardamos el resultado de la consulta

    if resultado:  # Comprobamos si hay un alumno en los resultados
        print("Alumno encontrado:", resultado)
    else:
        print("No se encontró un alumno con ese DNI.")

    return resultado  # Devolvemos el resultado (no la variable 'alumno')

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

def modificar_alumno():
    buscar_alumno_dni()
    
    opcion= int(input("elija la opcion que desea modificar: "))
    

    
    