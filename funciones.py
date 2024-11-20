from passlib.hash import sha256_crypt
import pymysql
#region conectarse
def conectarse()-> None:
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="NightcoreBlack04",
        db="integradora",
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
    password_cryp = sha256_crypt.hash(constraña)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(nombre, correo, contraseña, estatus) VALUES(%s, %s, %s, %s)",(nombre, correo, password_cryp, status))
    conexion.commit()
    conexion.close()
#guardarUsuario("patata", "patata@correo.com", "patata", "1")

def actualizarEstado(nombre:str, activo:int):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE status SET status =" + "'" + activo + "'" + "WHERE nombre = " + "'")
    conexion.commit()
    conexion.close()

def actualizarContraseña(nombre:str, contraña:str):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE contraña SET contraña = " + "'" + contraña + "'" + "WHERE nombre = " + "'")
    conexion.commit()
    conexion.close()

#endregion
#region setDatos
def guardarCombinacionesMulti(multiplexor:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO combinaciones(multiplexor) VALUES(%s, %s)",
                        (multiplexor))
    conexion.commit()
    conexion.close()

def guardarCombinacionesDemulti(demultiplexor:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO combinaciones(demultiplexor) VALUES(%s, %s)",
                     (demultiplexor))
    conexion.commit()
    conexion.close()
#endregion
#region getDatos
def comprobarUsuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre FROM usuario")
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

#print(comprobarUsuario())

def getPassword(nombre:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT contraseña FROM usuario Where nombre = " + "'" + nombre + "';")
        password = cursor.fetchone()
    conexion.close()
    pas = password.__getitem__(0)
    return pas

print(getPassword("patata"))

def getConceptos(materia:int)->str:
    concepts = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        conceptos1 = cursor.execute("SELECT titulo FROM conceptos WHERE idpagina =" + "'" + materia +"'")
        conceptos1 = cursor.fetchall()
        conceptos2 = cursor.execute("SELECT descripcion FROM conceptos WHERE idpagina =" + "'" + materia +"'")
        conceptos2 = cursor.fetchall()
    conexion.close() 
    for i in range(len(conceptos1)):
        concepts.append(conceptos1.__getitem__(i))
        concepts.append(conceptos2.__getitem__(i))
    return concepts

def getIDPagina(pagina:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        idPagina = cursor.execute("SELECT idpagina FROM pagina WHERE materia =" + "'" + pagina +"'")
        idPagina = cursor.fetchone()
    conexion.close() 
    idPag = idPagina.__getitem__(0)
    return idPag
#endregion

#region identificador
def identificar_ecuacion(ecuacion):
    # Simplificado para este ejemplo
    resultado = {
        "grado": "1" if "^" not in ecuacion else "2",  
        "orden": "2",  # Placeholder para orden
        "linealidad": "Lineal" if "y" in ecuacion and "^" not in ecuacion else "No lineal",
        "tipo": "Ordinaria" if "∂" not in ecuacion else "Parcial"
    }
    return resultado
#endregion