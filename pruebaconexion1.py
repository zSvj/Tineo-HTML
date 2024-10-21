import mysql.connector # type: ignore
from tkinter import messagebox
import os

def conectar_bd():
    try:
        # Load database credentials from environment variables
        host = os.environ.get('MYSQL_HOST', 'localhost')
        user = os.environ.get('MYSQL_USER', 'root')
        password = os.environ.get('MYSQL_PASSWORD', '')
        database = os.environ.get('MYSQL_DATABASE', 'proyecto')

        # Establish the database connection
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=12345,
            database=proyecto # type: ignore
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {err}")
        return None
    except Exception as err:
        messagebox.showerror("Error", f"An unexpected error occurred: {err}")
        return None

# Example usage:
conexion = conectar_bd()
if conexion:
    try:
        # Use the database connection
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proyecto")
        results = cursor.fetchall()
        for row in results:
            print(row)
    finally:
        # Close the database connection
        conexion.close()