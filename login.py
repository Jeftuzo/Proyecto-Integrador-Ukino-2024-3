import pymysql
from datetime import datetime

registro = {}

def conectarse()-> None:
    return pymysql.connect(
        host="127.0.0.0",
        user="root",
        passwd="Contraseña@123",
        db="baseatos",
    )
def inicio(usuario:str)->None:
    now =datetime.now()
    registro[usuario] = {"fecha y hora de inicio de sesion: ": now}