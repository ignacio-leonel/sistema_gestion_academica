import sqlite3

# Conectamos a una base de datos (si no existe, se crea automáticamente)
conexion = sqlite3.connect('universidad.db')

# Creamos un cursor para interactuar con la base de datos
cursor = conexion.cursor()

