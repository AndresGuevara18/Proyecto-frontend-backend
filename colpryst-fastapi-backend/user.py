#comando instlacion --- pip install fastapi uvicorn pydantic
from fastapi import APIRouter, HTTPException #APIRouter: Se utiliza para construir APIs con Python // HTTPException: Se utiliza para facilitar las notificaciones de errores. Cuando se lanza una excepción de tipo HTTPException
from pydantic import BaseModel #se utiliza para importar la clase BaseModel de la librería Pydantic
from connection import conectar

router = APIRouter() #Creación del enrutador para  las rutas relacionadas con los usuarios

# Establecer conexión a la base de datos
conexion = conectar()
if not conexion: #Si no se pudo establecer conexión, se lanza un error crítico
    raise RuntimeError("No se pudo conectar a la base de datos. Revisa la configuración.")

cursor = conexion.cursor() #Cursor para ejecutar consultas SQL en la base de datos

## Modelo de datos de usuario
class User(BaseModel):
    id: int
    tipoDocumento: str
    numeroDoc: str
    nombres: str
    email:str    
    entidad: int

#todos los usuarios
@router.get("/users/all")#ruta
async def get_all_users():# Función asíncrona para manejar la solicitud

    try:
        select_query = "SELECT * FROM Usuario" #consulta mysql
        cursor.execute(select_query) #ejecutar la consulta
        result = cursor.fetchall()  # fetchall() devuelve una lista de todos los registros de un conjunto de datos activo / Obtenemos todos los registros como una lista de tuplas
        if not result: #Si no hay resultados, lanza una excepción HTTP con código 404
            raise HTTPException(status_code=404, detail="No se encontraron usuarios")
        
        #  tuplas a lista de diccionarios
        users = []
        for row in result:
            users.append({
                #este modelo se usara para el front
                "id": row[0],
                "tipoDocumento": row[1],
                "numeroDoc": row[2],
                "nombres": row[3],
                "email": row[4],
                "entidad": row[5], 
            })
        return users
    except Exception as e:#xcepción HTTP con código 500 y el mensaje de error
        raise HTTPException(status_code=500, detail=f"Error al obtener los usuarios: {e}")

#usuario por id    
@router.get("/users/")
async def get_users(id: int):  # Recibimos el ID como parámetro
    try:
        select_query = "SELECT * FROM Usuario WHERE IdUsuario = %s" #consulta mysql donde id=?
        cursor.execute(select_query, (id,)) #ejecutar la consulta con parametro
        result = cursor.fetchone() # btenemos un solo registro
        if not result: ## Si no lanza error 404
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuario: {e}")

#agregar usuario
@router.post("/users/")
async def save_users(user: User): # Recibimos los datos validados en el cuerpo de la solicitud
    try:
        insert_query = """
        INSERT INTO Usuario (IdUsuario, Tipo_doc, numero_doc, Nombre_empleado, Email_empleado, IdCargoUsu)
        VALUES ( %s,%s, %s, %s, %s, %s)
        """ #insert mysql
        cursor.execute(insert_query, (user.id, user.tipoDocumento ,user.numeroDoc, user.nombres, user.email, user.entidad)) ## Ejecutarconsulta de inserción con los datos del modelo `User`
        conexion.commit() # Confirmar los cambios en la base de datos //  En Python, el método commit() se utiliza para guardar los cambios realizados en una base de datos
        return {"message": "Usuario guardado con éxito"} #mensaje 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar usuario: {e}")

#actualizar usuario
@router.patch("/users/{id}")
async def update_users(id: int, user: User): # Recibir el id y los datos a actualizar del modelo
    
    try:
        update_query = """
        UPDATE Usuario SET 
        Tipo_doc = %s,
        numero_doc = %s,
        Nombre_empleado = %s,
        Email_empleado = %s,
        IdCargoUsu = %s
        WHERE IdUsuario = %s
        """
        cursor.execute(update_query, (
            user.tipoDocumento,
            user.numeroDoc,
            user.nombres,
            user.email,
            user.entidad,
            id
        ))## Ejecutamos la consulta de actualización
        conexion.commit() # Confirmar los cambios en la base de datos //
        return {"message": f"Usuario con id {id} actualizado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar usuario: {e}")

#eliminar usuario
@router.delete("/users/{id}")
async def delete_users(id: int):  # Recibimos el ID como parámetro

    try:
        delete_query = "DELETE FROM Usuario WHERE IdUsuario = %s" ## Consulta SQL para eliminar por id
        cursor.execute(delete_query, (id,)) #Ejecutar la consulta
        conexion.commit() ## Confirmar l cambios en BD
        return {"message": f"Usuario con id {id} eliminado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar usuario: {e}")
