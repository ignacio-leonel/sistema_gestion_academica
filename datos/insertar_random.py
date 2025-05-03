import sqlite3
import random

# Función para obtener conexión
def obtener_conexion():
    return sqlite3.connect("sistema_gestion.db")

import sqlite3

def crear_tabla():
    # Conectamos a la base de datos
    conn = sqlite3.connect('sistema_gestion.db')
    cursor = conn.cursor()

    # Crear tabla alumnos si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            legajo INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            dni TEXT NOT NULL UNIQUE,
            carrera TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Tabla 'alumnos' creada correctamente si no existía.")

if __name__ == "__main__":
    crear_tabla()

nombres = ['Ana', 'Luis', 'María', 'Carlos', 'Laura', 'Diego', 'Sofía', 'Javier', 'Lucía', 'Matías']
apellidos = ['Gómez', 'Rodríguez', 'Fernández', 'López', 'Martínez', 'Pérez', 'Sánchez', 'Romero', 'Díaz', 'Alvarez']
carreras = [
    'Licenciatura en Gestión de Tecnologías de La Información',
    'Profesorado de Educación Física',
    'Licenciatura en Enfermería',
    'Abogacía',
    'Licenciatura en Videojuegos'
]

# Insertar alumnos
def insertar_alumnos():
    conn = obtener_conexion()
    cursor = conn.cursor()

    dni_usados = set()

    # Insertar 50 alumnos con legajos del 1 al 50
    for legajo in range(1, 51):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)

        # Generar DNI único
        dni = random.randint(20000000, 45000000)
        while dni in dni_usados:
            dni = random.randint(20000000, 45000000)
        dni_usados.add(dni)

        carrera = random.choice(carreras)

        cursor.execute(
            "INSERT INTO alumnos (legajo, nombre, apellido, dni, carrera) VALUES (?, ?, ?, ?, ?)",
            (legajo, nombre, apellido, str(dni), carrera)
        )

    conn.commit()
    print("✅ 50 alumnos insertados correctamente.")
    conn.close()

if __name__ == "__main__":
    insertar_alumnos()
