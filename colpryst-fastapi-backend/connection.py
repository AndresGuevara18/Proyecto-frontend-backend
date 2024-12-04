#comando instalar -- pip install pymssql
import pymysql

#funcion para conectar
def conectar():
    try:
        print("Intentando conectar con pymysql...")
         # Usamos `pymysql.connect` para conectarnos a la base de datos MySQL
        conexion = pymysql.connect(
            user="root",
            password="admin123",
            host="localhost",
            port=3306,
            database="ColprystFastApi"
        )
        print("¡Conexión exitosa con pymysql!")
        return conexion
    except pymysql.MySQLError as error: # Capturar errores relacionados con MySQL
        print(f"Error de MySQL: {error}")
        return None  # manejar return
    except Exception as e:
        print(f"Otro error ocurrió: {e}")
        return None