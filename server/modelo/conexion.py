import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "tienda_angular_python_lunargames"
    )
    # si conexion se ha realizado correctamente
    # contine un valor distinto a None
    if conexion:
        print("conexion con la base de datos OK")
        return conexion
    else:
        print("no pude conectar con la bd, comprueba los datos de la conexion")