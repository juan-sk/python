from datetime import datetime
import mysql.connector

import os
from dotenv import load_dotenv


def configs():
    try :
        print("cargando environment")
        load_dotenv()
    except Exception:
        raise Exception("ocurrio un error para cargar el archivo .env")

        
def conectarDB():
    try:

        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            password =os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )
        return mydb 
        
    except Exception:
      raise Exception("ocurrio un error conectandose a la db")

def insertarAlumno(mysql):

    cursor = mysql.cursor()
    query = '''
    INSERT INTO alumnos (id, nombre, apellido, fecha_nacimiento) VALUES (%s, %s, %s, %s);
    '''
    try:
    
        data = (1, 'Juan', 'Ramirez', datetime(1970, 4, 5))        
        cursor.execute(query, data)
        mysql.commit()
        print('{} se inserto'.format(cursor.rowcount))
        cursor.close()  
    except(Exception) as error:
       raise Exception("ocurrio un error al insertar el registro en la  db %s"% error)
       
def cerrarDB(mydb):
    if mydb is not None:
        mydb.close()
        print('se cerro la db')
def main():
    print("este programa se conecta a la base de datos")
    
    try:        
        print("cargando onfiguraciones")
        configs()
        print("configuraciones cargadas")
        print("conectando db")
        mydb = conectarDB()
    
        print("se logro conectar a la db")
        print(mydb)
        print("insertando registro")
        insertarAlumno(mydb)
        cerrarDB(mydb)   
    
            
    except Exception as error:
        cerrarDB(mydb)   
        print (error)


if __name__ == "__main__":
    main()  