from passlib.hash import sha256_crypt
import pymysql
#region conectarse
def conectarse()-> None:
    return pymysql.connect(
        host="127.0.0.0",
        user="root",
        passwd="Contraseña@123",
        db="baseatos",
    )

#endregion
#region usuario
class Usuario():
    def __init__(self, nombre:str, correo:str, constraña:str, status):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = constraña
        self.status = status

def guardarUsuario(nombre:str, correo:str, constraña:str, status):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(nombre, correo, contraseña, status) VALUES(%s, %s, %s)")
        (nombre, correo, constraña)
    conexion.commit()
    conexion.close()

def actualizarEstado(nombre:str, activo:int):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE status SET status =" + "'" + activo + "'" + "WHERE nombre = " + "'")
    conexion.commit()
    conexion.close()

def actualizarEstado(nombre:str, contraña:str):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE contraña SET contraña = " + "'" + contraña + "'" + "WHERE nombre = " + "'")
    conexion.commit()
    conexion.close()

#endregion
#region setDatos

#endregion
#region getDatos
def comprobar_usuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT usuario FROM usuarios")
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

def get_password(nombre:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT contraña FROM usuario =" + "'" + nombre + "'")
        password = cursor.fetchone()
    conexion.close()
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas

def get_conceptos()->str:
    concepts = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        conceptos1 = cursor.execute("SELECT titulo FROM conceptos")
        conseptos1 = cursor.fetchall()
        conceptos2 = cursor.execute("SELECT descripcion FROM conceptos")
        conseptos2 = cursor.fetchall()
    conexion.close()
    for i in range(len(conceptos1)):
        concepts.append(conceptos1.__getitem__(i))
        concepts.append(conceptos2.__getitem__(i))
    return concepts
#endregion