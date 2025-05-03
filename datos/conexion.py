import sqlite3

def conexion():
    return sqlite3.connect("datos/sistema_gestion.db")