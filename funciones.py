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
'''def conectarse()-> None:
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="JeftuzoTheKill2003",
        db="integrador",
    )'''

#endregion
#region usuario
class Usuario():
    def __init__(self, nombre:str, correo:str, constraña:str, status):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = constraña
        self.status = status

def guardarUsuario(nombre: str, correo: str, contraseña: str, status: str):
    password_cryp = sha256_crypt.hash(contraseña)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(nombre, correo, contraseña, estatus) VALUES(%s, %s, %s, %s)", (nombre, correo, password_cryp, status))
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
#region getDatos
def comprobarUsuario() -> list:
    c_us = []
    conexion = conectarse()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT nombre FROM usuario")
            c_usuario = cursor.fetchall()
        for i in range(len(c_usuario)):
            us = c_usuario[i][0]
            c_us.append(us)
    finally:
        conexion.close()
    return c_us



#print(comprobarUsuario())

def getPassword(nombre: str) -> str:
    conexion = conectarse()
    password = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT contraseña FROM usuario WHERE nombre = %s;", (nombre,))
            result = cursor.fetchone()
            if result:
                password = result[0]
    finally:
        conexion.close()
    return password



#print(getPassword("patata"))

def getConceptos(materia:str)->str:
    concepts = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        conceptos1 = cursor.execute("SELECT titulo FROM conceptos WHERE paginas =" + "'" + materia +"'")
        conceptos1 = cursor.fetchone()
        conceptos2 = cursor.execute("SELECT descripcion FROM conceptos WHERE paginas =" + "'" + materia +"'")
        conceptos2 = cursor.fetchone()

    conexion.close() 
    
    concepts.append(conceptos1.__getitem__(0))
    concepts.append(conceptos2.__getitem__(0))
    return concepts


    concepts = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        llaveforanea = cursor.execute("SELECT id FROM conceptos WHERE paginas =" + "'" + materia +"'")
        llaveforanea = cursor.fetchone()
        conceptos3 = cursor.execute("SELECT subtema FROM subtitulos WHERE paginas ="  + llaveforanea +"")
        conceptos3 = cursor.fetchall()
        conceptos4 = cursor.execute("SELECT descripcion FROM subtitulos WHERE paginas ="  + llaveforanea +"")
        conceptos4 = cursor.fetchall()

    conexion.close() 

    for i in range(len(conceptos3)):
        us1 = conceptos3.__getitem__(i)
        us2 = conceptos4.__gettitem__(i)
        concepts.append(us1.__getitem__(0))
        concepts.append(us2.__getitem__(0))
    return concepts

'''def getIDPagina(pagina:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        idPagina = cursor.execute("SELECT idpagina FROM pagina WHERE materia =" + "'" + pagina +"'")
        idPagina = cursor.fetchone()
    conexion.close() 
    idPag = idPagina.__getitem__(0)
    return idPag'''
#endregion

#region identificador
def identificar_ecuacion(ecuacion):
    # Simplificado para este ejemplo
    resultado = {
        "grado": "1" if "^" not in ecuacion else "2",  
        "orden": "2",  
        "linealidad": "Lineal" if "y" in ecuacion and "^" not in ecuacion else "No lineal",
        "tipo": "Ordinaria" if "∂" not in ecuacion else "Parcial"
    }
    return resultado
#endregion